"""Common step definitions used across features"""
from behave import given, then
from support.mock_api import setup_api_client

# ===========================
# Given Steps (Setup)
# ===========================
@given('I am authenticated as a sales user')
def step_authenticate_sales_user(context):
    """Authenticate as a sales user"""
    setup_api_client(context)
    
    auth_data = {
        "username": "sales_user",
        "password": "password123"
    }
    response = context.api_client.login(auth_data)
    
    assert response.status_code == 200, f"Login failed with status {response.status_code}"
    
    context.auth_token = response.json().get('token')
    context.api_client.set_auth_token(context.auth_token)

@given('the quote service is available')
def step_quote_service_available(context):
    """Ensure quote service is available"""
    setup_api_client(context)

@given('I have valid authentication')
def step_have_valid_auth(context):
    """Alias for authenticated user"""
    step_authenticate_sales_user(context)

@given('a customer exists with name "{customer_name}"')
def step_customer_exists_with_name(context, customer_name):
    """Ensure a customer exists with given name"""
    setup_api_client(context)
    response = context.api_client.get_customer_by_name(customer_name)
    assert response.status_code == 200
    context.customer_id = response.json().get('id')

@given('a customer with id "{customer_id}" exists')
def step_customer_exists_with_id(context, customer_id):
    """Ensure a customer exists with given ID"""
    setup_api_client(context)
    context.customer_id = customer_id

@given('a customer with id "{customer_id}" does not exist')
def step_customer_not_exists(context, customer_id):
    """Setup non-existent customer scenario"""
    setup_api_client(context)
    context.customer_id = customer_id

@given('performance monitoring is enabled')
def step_enable_performance_monitoring(context):
    """Enable performance monitoring"""
    context.performance_monitoring = True

@given('I have {count:d} items in my quote')
def step_have_n_items(context, count):
    """Generate N items for testing"""
    from support.api_client import QuoteHelpers
    context.items = QuoteHelpers.generate_items(count)

# ===========================
# Common Then Steps
# ===========================
@then('the response status should be {status_code:d}')
def step_verify_status_code(context, status_code):
    """Verify response status code"""
    assert context.response.status_code == status_code, \
        f"Expected status {status_code}, got {context.response.status_code}"

@then('the error message should be "{expected_message}"')
def step_verify_error_message(context, expected_message):
    """Verify exact error message"""
    data = context.response.json()
    actual_message = data.get('error', '')
    assert actual_message == expected_message, \
        f"Expected error '{expected_message}', got '{actual_message}'"

@then('the error message should contain "{expected_text}"')
def step_verify_error_contains(context, expected_text):
    """Verify error message contains text"""
    data = context.response.json()
    actual_message = data.get('error', '')
    assert expected_text in actual_message, \
        f"Expected error to contain '{expected_text}', got '{actual_message}'"