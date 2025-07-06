"""Environment setup for Behave tests"""
from unittest.mock import MagicMock, Mock

print("Loading environment.py file...")

class MockResponse:
    """Mock HTTP response"""
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        
    def json(self):
        return self.json_data


def before_all(context):
    print("Running before_all setup...")

    context.api_client = MagicMock()
    
    context.api_client.login = MagicMock(
        return_value=MockResponse({"token": "mock_token_123"}, 200)
    )
    
    context.api_client.set_auth_token = MagicMock()
    

    context.api_client.get_customer_by_name = MagicMock(
        return_value=MockResponse({"id": "customer_123", "name": "Test Customer"}, 200)
    )
    
    context.api_client.create_customer = MagicMock(
        return_value=MockResponse({"id": "customer_123", "name": "Test Customer"}, 201)
    )
    
    def mock_create_quote(quote_data):
        """Mock quote creation logic"""
        total = 0
        items_with_totals = []
        
        for item in quote_data['items']:
            quantity = item.get('quantity', 1)
            unit_price = item.get('unitPrice', 0)
            discount = item.get('discount', 0)
            
            subtotal = quantity * unit_price
            discount_amount = subtotal * (discount / 100)
            item_total = subtotal - discount_amount
            
            item_with_total = item.copy()
            item_with_total['total'] = item_total
            item_with_total['discountAmount'] = discount_amount
            items_with_totals.append(item_with_total)
            
            total += item_total
        
        return MockResponse({
            "id": "quote_123",
            "customerId": quote_data['customerId'],
            "items": items_with_totals,
            "total": total,
            "createdAt": "2024-01-01T10:00:00Z"
        }, 201)
    
    context.api_client.create_quote = mock_create_quote
    print("API client setup completed!")


def before_scenario(context, scenario):
    """Set up before each scenario"""
    print(f"Starting scenario: {scenario.name}")
    context.items = []
    context.customer_id = None
    context.auth_token = None