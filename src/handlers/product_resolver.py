from ..config import ID_MAPPING
from ..events import ItemAddedEvent, ProductIdResolvedEvent, ProductIdResolutionFailedEvent

class ProductResolver:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe(ItemAddedEvent, self.resolve_product_id)
    
    def resolve_product_id(self, event: ItemAddedEvent):
        try:
            product_id = ID_MAPPING.get(event.name)
            if product_id is None:
                self.event_bus.publish(
                    ProductIdResolutionFailedEvent(event.name, "Not found")
                )
            else:
                self.event_bus.publish(
                    ProductIdResolvedEvent(event.name, product_id)
                )
        except Exception as e:
            self.event_bus.publish(
                ProductIdResolutionFailedEvent(event.name, str(e))
            )