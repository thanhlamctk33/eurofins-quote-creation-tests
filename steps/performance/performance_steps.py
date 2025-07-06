from behave import when
import logging

logger = logging.getLogger(__name__)

@when('I create quotes with item "{item_name}" quantity {quantity:d} and price {price:f} over {duration:d} seconds')
def sustained_load_test(context, item_name, quantity, price, duration):
    pass

@when('{user_count:d} users create quotes simultaneously')
def concurrent_users_test(context, user_count):
    pass

@when('I suddenly send {request_count:d} concurrent requests within {duration:d} minute')
def spike_load_test(context, request_count, duration):
    pass

@when('I send {request_count:d} sequential requests')
def memory_leak_test(context, request_count):
    pass

@when('I create a quote with {item_count:d} items each having long descriptions')
def large_payload_test(context, item_count):
    pass

@when('I open {connection_count:d} concurrent connections and hold them for {duration:d} seconds')
def connection_pool_test(context, connection_count, duration):
    pass