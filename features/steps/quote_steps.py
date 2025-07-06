"""Step definitions for quote creation feature"""
from behave import given, when, then
from support.mock_api import setup_api_client
from support.api_client import QuoteHelpers

# ===========================
# Given Steps (Item Setup)
# ===========================
@given('one item with name "{item_name}"')
def step_one_item(context, item_name):
    """Set up single item"""
    context.items = [{
        "name": item_name,
        "description": f"Description for {item_name}"
    }]

@given('one item "{item_name}" with price {price:f}')
def step_one_item_with_price(context, item_name, price):
    """Set up single item with price"""
    context.items = [{
        "name": item_name,
        "unitPrice": price,
        "quantity": 1
    }]

@given('two items')
def step_two_items(context):
    """Set up two items from table"""
    context.items = []
    for row in context.table:
        context.items.append({
            "name": row['name'],
            "quantity": int(row['quantity']),
            "unitPrice": float(row['price'])
        })

@given('the following items')
def step_multiple_items(context):
    """Set up multiple items from detailed table"""
    context.items = []
    for row in context.table:
        item = {
            "name": row['name'],
            "quantity": float(row['quantity']),
            "unitPrice": float(row['price'])
        }
        if 'discount' in row.headings:
            item['discount'] = float(row['discount'])
        if 'description' in row.headings:
            item['description'] = row['description']
        context.items.append(item)

# ===========================
# When Steps (Actions)
# ===========================
@when('I create a quote for that customer with that item with quantity {quantity:d} and price {price:f}')
def step_create_quote_simple(context, quantity, price):
    """Create quote with single item"""
    setup_api_client(context)