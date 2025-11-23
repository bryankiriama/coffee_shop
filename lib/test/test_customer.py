
import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def setup_function():
    Order.clear_all()


def test_customer_validation():
    with pytest.raises(ValueError):
        Customer("")  # too short
    with pytest.raises(ValueError):
        Customer("x" * 16)  # too long
    with pytest.raises(TypeError):
        Customer(123)  # wrong type



def test_create_order_and_queries():
    brian = Customer("brian")
    latte = Coffee("Latte")
    brian.create_order(latte, 3.0)
    brian.create_order(latte, 4.0)
    assert len(brian.orders()) == 2
    assert latte in brian.coffees()
