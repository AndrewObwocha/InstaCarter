import unittest
from unittest.mock import Mock, patch

from src.events.events import (
	APIRequestFailedEvent,
	APISuccessEvent,
	ItemAddedEvent,
	PayloadReadyEvent,
	ProductIdResolvedEvent,
)
from src.handlers.api_client import APIClient
from src.handlers.payload_builder import PayloadBuilder
from src.handlers.product_resolver import ProductResolver


class TestProductResolver(unittest.TestCase):
	def test_resolve_product_id_publishes_resolved_event(self):
		event_bus = Mock()
		resolver = ProductResolver(event_bus)

		event = ItemAddedEvent(
			name="Tilda Basmati Rice",
			quantity=1,
			unit="kg",
		)
		resolver.resolve_product_id(event)

		published_event = event_bus.publish.call_args[0][0]
		self.assertIsInstance(published_event, ProductIdResolvedEvent)
		self.assertEqual(published_event.name, "Tilda Basmati Rice")
		self.assertEqual(published_event.product_id, 254990)

	def test_resolve_product_id_unknown_name_publishes_failure_event(self):
		event_bus = Mock()
		resolver = ProductResolver(event_bus)

		event = ItemAddedEvent(name="Unknown Item", quantity=1, unit="kg")
		resolver.resolve_product_id(event)

		published_event = event_bus.publish.call_args[0][0]
		self.assertEqual(type(published_event).__name__, "ProductIdResolutionFailedEvent")
		self.assertEqual(published_event.name, "Unknown Item")


class TestPayloadBuilder(unittest.TestCase):
	@patch("src.handlers.payload_builder.ID_MAPPING", {"A": 1, "B": 2})
	@patch("src.handlers.payload_builder.build_payload")
	def test_emits_payload_ready_after_all_items(self, mock_build_payload):
		mock_build_payload.return_value = {"line_items": ["complete"]}
		event_bus = Mock()
		builder = PayloadBuilder(event_bus)

		builder.add_to_payload(ProductIdResolvedEvent(name="A", product_id=1))
		event_bus.publish.assert_not_called()

		builder.add_to_payload(ProductIdResolvedEvent(name="B", product_id=2))

		event_bus.publish.assert_called_once()
		published_event = event_bus.publish.call_args[0][0]
		self.assertIsInstance(published_event, PayloadReadyEvent)
		self.assertEqual(published_event.payload, {"line_items": ["complete"]})


class TestAPIClient(unittest.TestCase):
	def test_send_request_success_publishes_api_success_event(self):
		event_bus = Mock()
		api_client = APIClient(event_bus)
		api_client._make_request = Mock(return_value={"ok": True})

		api_client.send_request(PayloadReadyEvent(payload={"line_items": []}))

		published_event = event_bus.publish.call_args[0][0]
		self.assertIsInstance(published_event, APISuccessEvent)
		self.assertEqual(published_event.response, {"ok": True})

	def test_send_request_failure_publishes_api_failed_event(self):
		event_bus = Mock()
		api_client = APIClient(event_bus)
		api_client._make_request = Mock(side_effect=RuntimeError("boom"))

		api_client.send_request(PayloadReadyEvent(payload={"line_items": []}))

		published_event = event_bus.publish.call_args[0][0]
		self.assertIsInstance(published_event, APIRequestFailedEvent)
		self.assertIn("boom", published_event.error)


if __name__ == "__main__":
	unittest.main()
