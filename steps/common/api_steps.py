from behave import when, then
import requests
import json
import logging

logger = logging.getLogger(__name__)

@when('I create a quote for that customer with that item with quantity {quantity:d} and price {price:f}')
def create_quote_single_item(context, quantity, price):
    payload = {
        'customer_id': context.customer['id'],
        'items': [{
            'item_id': context.item['id'],
            'quantity': quantity,
            'price': price
        }]
    }
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I create a quote for that customer with that item with quantity {quantity:d}, price {price:f}, and discount {discount:f}')
def create_quote_with_discount(context, quantity, price, discount):
    payload = {
        'customer_id': context.customer['id'],
        'items': [{
            'item_id': context.item['id'],
            'quantity': quantity,
            'price': price,
            'discount': discount
        }]
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I create a quote with quantity {quantity:d} and discount {discount:f}%')
def create_quote_percentage_discount(context, quantity, discount):
    item_price = context.item['price']
    item_total = quantity * item_price
    discount_amount = item_total * (discount / 100)
    
    payload = {
        'customer_id': context.customer['id'],
        'items': [{
            'item_id': context.item['id'],
            'quantity': quantity,
            'price': item_price,
            'discount': discount_amount
        }]
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I create a quote for that customer with these items')
@when('I create a quote with all items')
def create_quote_multiple_items(context):
    payload = {
        'customer_id': context.customer['id'],
        'items': context.quote_items
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I attempt to create a quote with quantity {quantity:d} price {price:f} and discount {discount:f}')
def attempt_create_quote_invalid_discount(context, quantity, price, discount):
    payload = {
        'customer_id': context.customer['id'],
        'items': [{
            'item_id': context.item['id'],
            'quantity': quantity,
            'price': price,
            'discount': discount
        }]
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I attempt to create a quote without customer ID')
def attempt_create_quote_no_customer(context):
    payload = {
        'items': [{
            'item_id': 1,
            'quantity': 1,
            'price': 100.00
        }]
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I attempt to create a quote with item "{item_name}" quantity {quantity:d} and price {price:f}')
def attempt_create_quote_invalid_data(context, item_name, quantity, price):
    # First create the item
    item_response = requests.post(
        f"{context.base_url}/items",
        json={'name': item_name, 'price': abs(price)},
        headers=context.headers
    )
    
    if item_response.status_code == 201:
        item_id = item_response.json()['id']
    else:
        item_id = 1
    
    payload = {
        'customer_id': context.customer['id'],
        'items': [{
            'item_id': item_id,
            'quantity': quantity,
            'price': price
        }]
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@when('I create a quote with item name "{item_name}"')
def create_quote_with_special_item(context, item_name):
    item_response = requests.post(
        f"{context.base_url}/items",
        json={'name': item_name, 'price': 100.00},
        headers=context.headers
    )
    
    item_id = item_response.json()['id']
    
    payload = {
        'customer_id': context.customer['id'],
        'items': [{
            'item_id': item_id,
            'quantity': 1,
            'price': 100.00
        }]
    }
    
    context.response = requests.post(
        f"{context.base_url}/quotes",
        json=payload,
        headers=context.headers
    )

@then('the quote total should be {expected_total:f}')
def verify_quote_total(context, expected_total):
    assert context.response.status_code == 201, \
        f"Expected status 201, got {context.response.status_code}: {context.response.text}"
    quote_data = context.response.json()
    actual_total = float(quote_data['total'])
    
    # Allow small floating point differences
    assert abs(actual_total - expected_total) < 0.01, \
        f"Expected total {expected_total}, got {actual_total}"

@then('the response status code should be {status_code:d}')
def verify_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected status {status_code}, got {context.response.status_code}"

@then('the error message should be "{expected_message}"')
def verify_exact_error_message(context, expected_message):
    response_data = context.response.json()
    actual_message = response_data.get('error', response_data.get('message', ''))
    
    assert actual_message == expected_message, \
        f"Expected message '{expected_message}', got '{actual_message}'"

@then('the error message should contain "{expected_text}"')
def verify_error_contains(context, expected_text):
    response_data = context.response.json()
    actual_message = response_data.get('error', response_data.get('message', ''))
    
    assert expected_text in actual_message, \
        f"Expected '{expected_text}' in message, got '{actual_message}'"