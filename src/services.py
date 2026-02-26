import http.client
import json
from typing import Any
from utils import headers, insert_items_into_payload


def call_instacart_api() -> None:
    payload_dict: dict[str, Any] = insert_items_into_payload()

    conn: http.client.HTTPSConnection = http.client.HTTPSConnection("connect.instacart.com")
    
    payload: str = json.dumps(payload_dict)

    conn.request("POST", "/idp/v1/products/products_link", payload, headers)

    res: http.client.HTTPResponse = conn.getresponse()
    
    data: bytes = res.read()

    print(data.decode("utf-8"))

