import logging
from typing import Callable, List

logger = logging.getLogger(__name__)

class EventBus:
    def __init__(self):
        self.handlers: dict = {}
        logger.info("EventBus initialized")
    
    def subscribe(self, event_type, handler: Callable):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)
        logger.debug(f"Subscribed {handler.__name__} to {event_type.__name__}")
    
    def publish(self, event):
        event_type = type(event)
        logger.debug(f"Publishing event: {event_type.__name__}")
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                handler(event)