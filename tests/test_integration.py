import unittest
from unittest.mock import patch

from src.events.events import APISuccessEvent, ItemAddedEvent
from src.handlers.api_client import APIClient
from src.handlers.payload_builder import PayloadBuilder
from src.handlers.product_resolver import ProductResolver
from src.infra.event_bus import EventBus


class TestIntegrationFlow(unittest.TestCase):
	@patch("src.handlers.payload_builder.ID_MAPPING", {"Tilda Basmati Rice": 254990})
	def test_end_to_end_event_flow_publishes_success(self):
		event_bus = EventBus()
		ProductResolver(event_bus)
		PayloadBuilder(event_bus)
		api_client = APIClient(event_bus)
		api_client._make_request = lambda payload: {"status": "ok", "payload": payload}

		received = []
		event_bus.subscribe(APISuccessEvent, lambda event: received.append(event))

		event_bus.publish(ItemAddedEvent(name="Tilda Basmati Rice", quantity=1, unit="kg"))

		self.assertEqual(len(received), 1)
		self.assertEqual(received[0].response["status"], "ok")
		self.assertIn("line_items", received[0].response["payload"])
		self.assertEqual(len(received[0].response["payload"]["line_items"]), 1)


if __name__ == "__main__":
	unittest.main()
