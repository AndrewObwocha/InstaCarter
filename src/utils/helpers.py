from typing import Any
from copy import deepcopy
from ..config import BASE_PAYLOAD

def build_payload(items: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the final payload for Instacart API"""
    payload = deepcopy(BASE_PAYLOAD)
    payload["line_items"] = items
    return payload

__all__ = ['build_payload']