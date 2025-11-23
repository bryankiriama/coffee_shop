
from order import Order


class Customer:
    """
    Customer with a validated name. Provides helpers to create orders and to query
    customer's orders and coffees. Also implements most_aficionado class method.
    """

    def __init__(self, name: str):
        self._name = None
        self.name = name  # use property setter for validation

    # name property with validation: string length 1..15
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        if not isinstance(val, str):
            raise TypeError("name must be a string.")
        trimmed = val.strip()
        if len(trimmed) < 1 or len(trimmed) > 15:
            raise ValueError("name must be between 1 and 15 characters.")
        self._name = trimmed

    # relationship methods
    def orders(self):
        """Return list of Order instances for this customer."""
        return [o for o in Order.all() if o.customer is self]

    def coffees(self):
        """Return unique list of Coffee instances this customer has ordered (preserve first-seen order)."""
        seen = set()
        unique = []
        for o in self.orders():
            c = o.coffee
            if id(c) not in seen:
                seen.add(id(c))
                unique.append(c)
        return unique

    def create_order(self, coffee, price: float):
        """
        Create a new Order associated with this customer and the given coffee.
        Returns the created Order instance.
        """
        # Order constructor will validate coffee and price
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Returns the Customer who has spent the most on the provided coffee
        (summing prices of orders where order.coffee is the provided coffee).
        Returns None if no orders exist for that coffee.
        """
        # Build totals per customer
        totals = {}
        for o in Order.all():
            if o.coffee is coffee:
                totals[o.customer] = totals.get(o.customer, 0.0) + o.price

        if not totals:
            return None

        # find customer with max total (ties -> first encountered with max)
        best_customer = max(totals.items(), key=lambda kv: kv[1])[0]
        return best_customer

    def __repr__(self):
        return f"Customer(name={self.name!r})"
