@given('the following items with absolute discounts')
def create_multiple_items(context):
    context.items = []
    context.quote_items = []
    
    for row in context.table:
        item_payload = {
            'name': row['name'],
            'price': float(row['price'])
        }
        
        item_response = requests.post(
            f"{context.base_url}/items",
            json=item_payload,
            headers=context.headers
        )
        
        assert item_response.status_code == 201, \
            f"Failed to create item {row['name']}: {item_response.status_code}"
        
        item = item_response.json()
        context.items.append(item)
        quote_item = {
            'item_id': item['id'],
            'quantity': float(row['quantity']),
            'price': float(row['price'])
        }
        if 'discount' in row.headings:
            quote_item['discount'] = float(row['discount'])
        
        context.quote_items.append(quote_item)
    
    logger.info(f"Created {len(context.items)} items")