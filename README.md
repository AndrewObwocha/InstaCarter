# Instacart-Auto-Shopper

Posts a fixed weekly shopping list to Instacart through their Connect API.
Meant to run unattended, triggered by cron or any other scheduler.

## How it works

`src/main.py` wires up an in-process event bus and three handlers, then
publishes one event per item in a hardcoded product list:

```
ItemAddedEvent          → ProductResolver  → ProductIdResolvedEvent
ProductIdResolvedEvent  → PayloadBuilder   → PayloadReadyEvent (once every item has resolved)
PayloadReadyEvent       → APIClient        → POST to Instacart, then a success/failure event
```

- **ProductResolver** looks up each item's Instacart product ID in
  `ID_MAPPING` (`src/config.py`).
- **PayloadBuilder** collects resolved items and only builds the final
  payload once every item in `ID_MAPPING` has resolved.
- **APIClient** posts that payload to Instacart's `products_link` endpoint
  and logs the result.

Nothing subscribes to the success/failure events besides the logger, so
`python -m src.main` exits `0` whether or not the post actually succeeded —
the log file is the only record of the outcome.

## Project structure

```
├── src/
│   ├── main.py              # wires up the event bus and starts the run
│   ├── config.py             # API URL, API key, item→product-ID map, payload template
│   ├── events/events.py      # event dataclasses
│   ├── infra/event_bus.py    # publish/subscribe bus
│   ├── handlers/
│   │   ├── product_resolver.py
│   │   ├── payload_builder.py
│   │   └── api_client.py
│   └── utils/helpers.py      # build_payload()
├── tests/
│   ├── config_test.py        # discovers and runs the other test_*.py files
│   ├── test_event_bus.py
│   ├── test_handlers.py
│   └── test_integration.py
├── scripts/
│   ├── run_instacart.sh
│   └── test_instacart.sh
├── Makefile
└── requirements.txt
```

## Prerequisites

- Python 3.9 or later — `config.py` uses builtin generics (`dict[str, int]`)
  as variable annotations, which Python evaluates eagerly and only supports
  from 3.9 onward.
- An Instacart Connect API key.

## Setup

```bash
git clone https://github.com/aobwocha/Instacart-Auto-Shopper.git
cd Instacart-Auto-Shopper
make setup      # creates venv/ and installs requirements.txt into it
```

Create a `.env` file in the project root with your API key — `config.py`
loads it via `python-dotenv`:

```
INSTACART_API_KEY=your_key_here
```

Both `scripts/run_instacart.sh` and `scripts/test_instacart.sh` append their
output to a `logs/` directory that isn't created automatically. Make it once
before the first run:

```bash
mkdir -p logs
```

## Running

```bash
make run
```

This runs `scripts/run_instacart.sh`, which activates `venv/` and runs
`python -m src.main`, appending stdout and stderr to `logs/run_instacart.log`.
Because the script resolves its own project root from its file location, you
can also call it directly by absolute path — useful for cron:

```
30 7 * * 5 /full/path/to/Instacart-Auto-Shopper/scripts/run_instacart.sh
```

## Testing

```bash
make test
```

This runs `scripts/test_instacart.sh`, which activates `venv/` and runs
`tests/config_test.py` — a small unittest runner that discovers and executes
every `test_*.py` file in `tests/` and appends the results to
`logs/test_instacart.log`.

## Changing the shopping list

The list of items, their Instacart product IDs, and the payload template
(retail store, list title, pantry-item setting) all live in
`ID_MAPPING` and `BASE_PAYLOAD` in `src/config.py`. There's no CLI or config
file for this — editing that dict is the only way to change what gets
ordered.

## Known limitations

- Every line item is submitted as quantity `1`, unit `kg`, regardless of the
  quantity and unit passed into `ItemAddedEvent` — `PayloadBuilder` hardcodes
  both values rather than using the ones on the event.
- If an item's name isn't in `ID_MAPPING`, `ProductResolver` publishes a
  failure event that nothing else subscribes to, and `PayloadBuilder` keeps
  waiting for a full set of successes — so the whole run stops silently,
  with only a log warning to show for it. This can't happen with the current
  `main.py`, since it publishes item names straight from `ID_MAPPING.keys()`,
  but it would surface if the item list ever came from another source.
- `BASE_PAYLOAD["landing_page_configuration"]["partner_linkback_url"]` is
  still the literal placeholder `"string"`. Update it in `src/config.py` if
  you want a real callback URL.
