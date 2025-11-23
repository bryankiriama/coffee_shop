from typing import List


class Order:

    _orders: List["Order"] = []

    def __init__(self, customer, coffee, price: float):
        """Validate types (customer and coffee are expected to be instances of Customer and Coffee)."""

        if customer is None or coffee is None:
            raise TypeError("customer and coffee must be provided (non-None).")

        # price validation
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number.")
        price = float(price)
        if price < 1.0 or price > 10.0:
            raise ValueError("price must be between 1.0 and 10.0 inclusive.")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        # append to class-level list (single source of truth)
        Order._orders.append(self)

    # properties
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all(cls):
        """Return all Order instances."""
        return list(cls._orders)
        return list(cls._orders)
    @classmethod
    def clear_all(cls):
        """Clear all stored orders."""
        cls._orders.clear()
        cls._orders.clear()
