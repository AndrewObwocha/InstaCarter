from typing import Callable, List

class EventBus:
    def __init__(self):
        self.handlers: dict = {}
    
    def subscribe(self, event_type, handler: Callable):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)
    
    def publish(self, event):
        event_type = type(event)
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                handler(event)