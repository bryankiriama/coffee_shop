from typing import List
from order import Order


class Coffee:
    """
    Coffee with a validated name. Provides helpers to query orders and customers,
    compute number of orders and average price.
    """

    def __init__(self, name: str):
        self._name = None
        self.name = name

    # name property validation: string length >= 3
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        if not isinstance(val, str):
            raise TypeError("name must be a string.")
        trimmed = val.strip()
        if len(trimmed) < 3:
            raise ValueError("coffee name must be at least 3 characters long.")
        self._name = trimmed

    # relationship methods
    def orders(self):
        """Return list of Order instances for this coffee."""
        return [o for o in Order.all() if o.coffee is self]

    def customers(self):
        """Return unique list of Customer instances who ordered this coffee (preserve first-seen order)."""
        seen = set()
        unique = []
        for o in self.orders():
            c = o.customer
            if id(c) not in seen:
                seen.add(id(c))
                unique.append(c)
        return unique

    # aggregate methods
    def num_orders(self) -> int:
        """Return total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self) -> float:
        """Return average price for this coffee's orders. 0.0 if none."""
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(o.price for o in orders)
        return total / len(orders)

    def __repr__(self):
        return f"Coffee(name={self.name!r})"
