import os
from dotenv import load_dotenv
from typing import Any

load_dotenv()

API_URL = "https://connect.instacart.com/idp/v1/products/products_link"
API_KEY = os.getenv("INSTACART_API_KEY")

ID_MAPPING: dict[str, int] = {
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

BASE_PAYLOAD: dict[str, Any] = {
    "title": "Weekly shopping list",
    "link_type": "shopping_list",
    "expires_in": 100,
    "instructions": ["Primary retail store is Walmart"],
    "line_items": [],
    "landing_page_configuration": {
        "partner_linkback_url": "string",
        "enable_pantry_items": True
    }
}

HEADERS: dict[str, str] = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': f"Bearer {API_KEY}"
}
