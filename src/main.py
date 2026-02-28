import logging
from .infra import EventBus
from .handlers import ProductResolver, PayloadBuilder, APIClient
from .events import ItemAddedEvent
from .config import ID_MAPPING

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    """Initialize event bus and handlers, then start the flow"""
    logger.info("Starting InstaCarter application")
    event_bus = EventBus()
    
    logger.info("Initializing handlers")
    ProductResolver(event_bus)
    PayloadBuilder(event_bus)
    APIClient(event_bus)
    
    logger.info(f"Publishing {len(ID_MAPPING)} item events")
    for item_name in ID_MAPPING.keys():
        event_bus.publish(ItemAddedEvent(item_name, 1, "kg"))
    
    logger.info("All items processed")


if __name__ == "__main__":
    main()
