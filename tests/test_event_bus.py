import unittest
import logging

from src.events.events import ItemAddedEvent
from src.infra.event_bus import EventBus

logger = logging.getLogger(__name__)


class TestEventBus(unittest.TestCase):
	def test_subscribe_and_publish_calls_handler(self):
		logger.info("Running: test_subscribe_and_publish_calls_handler")
		event_bus = EventBus()
		received = []

		def handler(event):
			received.append(event)

		event_bus.subscribe(ItemAddedEvent, handler)
		event = ItemAddedEvent(name="Milk", quantity=1, unit="L")

		event_bus.publish(event)

		self.assertEqual(len(received), 1)
		self.assertIs(received[0], event)
		logger.info("✓ test_subscribe_and_publish_calls_handler passed")

	def test_publish_without_subscribers_is_noop(self):
		logger.info("Running: test_publish_without_subscribers_is_noop")
		event_bus = EventBus()
		event = ItemAddedEvent(name="Eggs", quantity=12, unit="pcs")

		event_bus.publish(event)

		self.assertEqual(event_bus.handlers, {})
		logger.info("✓ test_publish_without_subscribers_is_noop passed")

	def test_multiple_handlers_are_called(self):
		logger.info("Running: test_multiple_handlers_are_called")
		event_bus = EventBus()
		calls = []

		def handler_one(event):
			calls.append(("one", event.name))

		def handler_two(event):
			calls.append(("two", event.name))

		event_bus.subscribe(ItemAddedEvent, handler_one)
		event_bus.subscribe(ItemAddedEvent, handler_two)

		event_bus.publish(ItemAddedEvent(name="Bread", quantity=1, unit="loaf"))

		self.assertEqual(calls, [("one", "Bread"), ("two", "Bread")])
		logger.info("✓ test_multiple_handlers_are_called passed")


if __name__ == "__main__":
	unittest.main()
