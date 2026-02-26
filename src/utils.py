import os
from dotenv import load_dotenv
from typing import Any

load_dotenv() 

id_mapping: dict[str, int] = {
    "Tilda Basmati Rice": 254990,
    "Your Fresh Market Lean Ground Beef": 19677688,
    "Hormel Classic Stagg Chili With Beans": 17886241,
    "Boneless Skinless Chicken Breasts": 19070600,
    "Hunt's Original Tomato Paste": 17819818,
    "Aylmer Crushed Tomatoes": 20726442,
    "Your Fresh Market Onion Yellow": 19305346,
    "Oasis Apple Juice": 19130709,
    "Great Value 100% Whole Wheat Bread": 34314531,
    "Great Value Extra Large White Eggs": 19070492,
    "Your Fresh Market California Mandarins": 2582509,
    "Great Value Extra Virgin Olive Oil Cooking Spray": 29493972,
}


payload_dict: dict[str, Any] = {
    "title": "Weekly shopping list",                  # str
    "link_type": "shopping_list",                     # str
    "expires_in": 100,                                # int
    "instructions": [                                 # list
        "Primary retail store is Walmart"
    ],
    "line_items": [],                                 # list of dicts
    "landing_page_configuration": {                   # dict
        "partner_linkback_url": "string",
        "enable_pantry_items": True
    }
}


headers: dict[str, str] = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': f"Bearer {os.getenv('INSTACART_API_KEY')}"
}


def insert_items_into_payload() -> dict[str, Any]:
    global payload_dict

    line_item: list[dict[str, Any]] = []

    for index, value in id_mapping.items():
        line_item.append({
            "name": index,
            "quantity": "1",
            "unit": "kg",
            "product_id": str(value)
        })

    payload_dict["line_items"] = line_items

    return payload_dict

