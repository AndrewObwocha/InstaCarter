import requests
from ..config import API_URL, HEADERS
from ..events import PayloadReadyEvent, APISuccessEvent, APIRequestFailedEvent

class APIClient:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe(PayloadReadyEvent, self.send_request)
    
    def _make_request(self, payload: dict):
        """Make HTTP POST request to Instacart API"""
        response = requests.post(API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    
    def send_request(self, event: PayloadReadyEvent):
        try:
            response = self._make_request(event.payload)
            self.event_bus.publish(APISuccessEvent(response))
        except Exception as e:
            self.event_bus.publish(APIRequestFailedEvent(str(e)))