from infra import EventBus
from handlers import ProductResolver, PayloadBuilder, APIClient
from events import ItemAddedEvent
from config import ID_MAPPING


def main():
    """Initialize event bus and handlers, then start the flow"""
    event_bus = EventBus()
    
    ProductResolver(event_bus)
    PayloadBuilder(event_bus)
    APIClient(event_bus)
    
    for item_name in ID_MAPPING.keys():
        event_bus.publish(ItemAddedEvent(item_name, 1, "kg"))


if __name__ == "__main__":
    main()
