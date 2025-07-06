from behave import given
import requests
import logging

logger = logging.getLogger(__name__)

@given('a customer exists with name "{customer_name}"')
def create_customer(context, customer_name):
    payload = {'name': customer_name}
    
    response = requests.post(
        f"{context.base_url}/customers",
        json=payload,
        headers=context.headers
    )
    assert response.status_code == 201, \
        f"Failed to create customer: {response.status_code} - {response.text}"
    
    context.customer = response.json()
    logger.info(f"Created customer: {context.customer['id']}")

@given('{count:d} customers exist for concurrent testing')
def create_multiple_customers(context, count):
    context.customers = []
    
    for i in range(count):
        payload = {'name': f'Concurrent Test Customer {i}'}
        
        response = requests.post(
            f"{context.base_url}/customers",
            json=payload,
            headers=context.headers
        )
        
        assert response.status_code == 201, \
            f"Failed to create customer {i}: {response.status_code}"
        
        context.customers.append(response.json())
    logger.info(f"Created {count} customers for concurrent testing")