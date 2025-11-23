
import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def setup_function():
    # clear orders before each test
    Order.clear_all()


def test_order_creation_and_properties():
    c = Customer("brian")
    coffee = Coffee("Mocha")
    order = Order(c, coffee, 2.5)
    assert order.customer is c
    assert order.coffee is coffee
    assert order.price == 2.5
    assert order in Order.all()
