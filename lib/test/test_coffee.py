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
    brian = Customer("brian")
    kiriama = Customer("kiriama")
    espresso = Coffee("Espresso")
    brian.create_order(espresso, 3.0)
    brian.create_order(espresso, 3.5)
    kiriama.create_order(espresso, 4.0)

    assert espresso.num_orders() == 3
    assert pytest.approx(espresso.average_price(), 0.0001) == (3.0 + 3.5 + 4.0) / 3
    customers = espresso.customers()
    assert brian in customers and kiriama in customers
