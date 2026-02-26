import http.client
import json
from typing import Any

from models import LineItem 
from utils import headers, insert_items_into_payload


def parse_line_item(item_list: list[LineItem]) -> list[dict[str, Any]]:
    line_item: list[dict[str, Any]] = []
    
    for item in item_list:
        line_item.append({
            "name": item.get_name(),
            "quantity": item.get_quantity(),
            "unit": item.get_unit(),
            "product_id": item.get_product_id()
        })
    
    return line_item


def call_instacart_api(item_list: list[LineItem]) -> None:
    line_item: list[dict[str, Any]] = parse_line_item(item_list)

    payload_dict: dict[str, Any] = insert_items_into_payload(line_item)

    conn: http.client.HTTPSConnection = http.client.HTTPSConnection("connect.instacart.com")
    
    payload: str = json.dumps(payload_dict)

    conn.request("POST", "/idp/v1/products/products_link", payload, headers)

    res: http.client.HTTPResponse = conn.getresponse()
    
    data: bytes = res.read()

    print(data.decode("utf-8"))

