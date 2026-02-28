import logging
from ..config import ID_MAPPING
from ..events import ItemAddedEvent, ProductIdResolvedEvent, ProductIdResolutionFailedEvent

logger = logging.getLogger(__name__)

class ProductResolver:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe(ItemAddedEvent, self.resolve_product_id)
        logger.info("ProductResolver initialized")
    
    def resolve_product_id(self, event: ItemAddedEvent):
        try:
            product_id = ID_MAPPING.get(event.name)
            if product_id is None:
                logger.warning(f"Product ID not found for: {event.name}")
                self.event_bus.publish(
                    ProductIdResolutionFailedEvent(event.name, "Not found")
                )
            else:
                logger.info(f"Resolved product ID {product_id} for: {event.name}")
                self.event_bus.publish(
                    ProductIdResolvedEvent(event.name, product_id)
                )
        except Exception as e:
            logger.error(f"Error resolving product ID for {event.name}: {e}")
            self.event_bus.publish(
                ProductIdResolutionFailedEvent(event.name, str(e))
            )