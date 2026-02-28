from ..config import ID_MAPPING
from ..utils import build_payload
from ..events import ProductIdResolvedEvent, PayloadReadyEvent

class PayloadBuilder:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.items = []
        self.event_bus.subscribe(ProductIdResolvedEvent, self.add_to_payload)
    
    def add_to_payload(self, event: ProductIdResolvedEvent):
        self.items.append({
            "name": event.name,
            "product_id": str(event.product_id),
            "quantity": "1",
            "unit": "kg"
        })
        if len(self.items) == len(ID_MAPPING):
            payload = build_payload(self.items)
            self.event_bus.publish(PayloadReadyEvent(payload))