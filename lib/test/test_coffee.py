import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def setup_function():
    Order.clear_all()


def test_coffee_validation():
    with pytest.raises(ValueError):
        Coffee("aa")
    with pytest.raises(TypeError):
        Coffee(123)


def test_aggregates_and_customers():
    alice = Customer("brian")
    bob = Customer("kiriama")
    espresso = Coffee("Espresso")
    alice.create_order(espresso, 3.0)
    alice.create_order(espresso, 3.5)
    bob.create_order(espresso, 4.0)

    assert espresso.num_orders() == 3
    assert pytest.approx(espresso.average_price(), 0.0001) == (3.0 + 3.5 + 4.0) / 3
    customers = espresso.customers()
    assert alice in customers and bob in customers
