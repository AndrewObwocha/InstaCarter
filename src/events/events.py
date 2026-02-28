from dataclasses import dataclass
from typing import Any

@dataclass
class ItemAddedEvent:
    name: str
    quantity: int
    unit: str

@dataclass
class ProductIdResolvedEvent:
    name: str
    product_id: int

@dataclass
class ProductIdResolutionFailedEvent:
    name: str
    error: str

@dataclass
class PayloadReadyEvent:
    payload: dict[str, Any]

@dataclass
class APIRequestFailedEvent:
    error: str

@dataclass
class APISuccessEvent:
    response: dict[str, Any]