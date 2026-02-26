# InstaCarter: Scheduled Instacart Shopping List Automation

## Hands-free weekly shopping list management.

InstaCarter is an automated Python application that generates and submits Instacart shopping lists on a scheduled basis. Running as a cron job, the application seamlessly creates shopping lists with predefined items, handling product mapping and API integration automatically. No manual intervention required.

- **Scheduled Automation** - Executes automatically every Friday at 7:30 AM via cron job.
- **Intelligent Product Mapping** - Maps product names to Instacart product IDs for reliable list creation.
- **Hands-Free Operation** - Runs in the background without CLI interaction or user prompts.

## Setup and Configuration

### Prerequisites

1. **Python 3.8+** - Required for running the application
2. **Instacart API Credentials** - API key must be configured in `utils.py`
3. **Unix-like Environment** - macOS, Linux, or WSL on Windows

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AndrewObwocha/InstaCarter.git
   cd InstaCarter
   ```

2. **Update Configuration:**
   - Set your Instacart API key in `utils.py` (replace `<API-key>` in the headers)
   - Define your shopping items in `models.py` or the main execution logic

3. **Make the script executable:**

   ```bash
   chmod +x run_instacart.sh
   ```

4. **Setup the Cron Job:**

   Open your crontab editor:

   ```bash
   crontab -e
   ```

   Add the following line to execute `run_instacart.sh` every Friday at 7:30 AM:

   ```
   30 7 * * 5 /path/to/InstaCarter/run_instacart.sh
   ```

   Replace `/path/to/InstaCarter` with the full absolute path to the InstaCarter directory.

### Manual Execution

To run the application manually outside of the scheduled cron job:

```bash
./run_instacart.sh
```

## Project Structure

- `main.py` - Core application logic for shopping list generation and submission
- `models.py` - `LineItem` class representing shopping items
- `services.py` - Instacart API communication and payload construction
- `utils.py` - Product ID mappings, API headers, and payload templates
- `run_instacart.sh` - Executable shell script for cron job integration
- `logs/` - Application execution logs and error tracking

## Monitoring and Troubleshooting

Check the `logs/` directory for execution records and any errors encountered during scheduled runs.

## Contributing

We welcome contributions! Here's how you can help:

1. **Report Issues** - Found a bug? Use the Issues tab with details about the behavior and environment.
2. **Submit Enhancements** - Have a feature idea? Open an issue to discuss the approach.
3. **Submit Pull Requests** - For bug fixes or features:
   - Create a new branch from `main`
   - Make your changes with clear commit messages
   - Submit a PR referencing any related issues
   - Ensure code follows the existing style

### Areas for Contribution

- Expand the product ID mapping database
- Improve error logging and monitoring
- Add error recovery mechanisms
- Support for multiple shopping lists or profiles
- Integration with other grocery services

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
