import requests
from typing import Dict, Optional, Any, List
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

class APIClient:
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth_token = None
        
    def set_auth_token(self, token: str):
        self.auth_token = token
        self.session.headers.update({
            'Authorization': f'Bearer {token}'
        })
        
    def post(self, endpoint: str, data: Dict[str, Any], 
        headers: Optional[Dict] = None, timeout: int = 30) -> requests.Response:
        url = urljoin(self.base_url, endpoint)
        headers = headers or {}
        headers['Content-Type'] = 'application/json'
        
        try:
            response = self.session.post(
                url, 
                json=data, 
                headers=headers,
                timeout=timeout
            )
            logger.debug(f"POST {endpoint} - Status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"POST {endpoint} failed: {e}")
            raise
            
    def get(self, endpoint: str, params: Optional[Dict] = None,
        headers: Optional[Dict] = None, timeout: int = 30) -> requests.Response:
        url = urljoin(self.base_url, endpoint)
        
        try:
            response = self.session.get(
                url,
                params=params,
                headers=headers,
                timeout=timeout
            )
            logger.debug(f"GET {endpoint} - Status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"GET {endpoint} failed: {e}")
            raise
            
    def create_quote(self, customer_id: Optional[int], items: List[Dict]) -> requests.Response:
        data = {'items': items}
        if customer_id:
            data['customer_id'] = customer_id
            
        return self.post('/quotes', data)
        
    def create_customer(self, name: str) -> requests.Response:
        return self.post('/customers', {'name': name})
        
    def create_item(self, name: str, price: float) -> requests.Response:
        """Create an item"""
        return self.post('/items', {'name': name, 'price': price})