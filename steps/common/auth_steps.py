from behave import given
import requests
import logging

logger = logging.getLogger(__name__)

@given('I am authenticated as a sales user')
def authenticate_user(context):
    auth_url = f"{context.base_url}/auth/login"
    credentials = {
        'username': context.config.get('TEST_USER', 'sales_user'),
        'password': context.config.get('TEST_PASSWORD', 'password123')
    }
    try:
        response = requests.post(auth_url, json=credentials)
        response.raise_for_status()
        
        auth_data = response.json()
        context.auth_token = auth_data['token']
        context.headers = {
            'Authorization': f'Bearer {context.auth_token}',
            'Content-Type': 'application/json'
        }
        logger.info("Authentication successful")
    except Exception as e:
        logger.error(f"Authentication failed: {e}")
        raise