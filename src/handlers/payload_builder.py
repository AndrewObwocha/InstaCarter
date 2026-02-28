import logging
from ..config import ID_MAPPING
from ..utils import build_payload
from ..events import ProductIdResolvedEvent, PayloadReadyEvent

logger = logging.getLogger(__name__)

class PayloadBuilder:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.items = []
        self.event_bus.subscribe(ProductIdResolvedEvent, self.add_to_payload)
        logger.info("PayloadBuilder initialized")
    
    def add_to_payload(self, event: ProductIdResolvedEvent):
        self.items.append({
            "name": event.name,
            "product_id": str(event.product_id),
            "quantity": "1",
            "unit": "kg"
        })
        logger.info(f"Added item to payload: {event.name} ({len(self.items)}/{len(ID_MAPPING)})")
        if len(self.items) == len(ID_MAPPING):
            payload = build_payload(self.items)
            logger.info(f"Payload complete with {len(self.items)} items, publishing PayloadReadyEvent")
            self.event_bus.publish(PayloadReadyEvent(payload))