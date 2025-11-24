

from order import Order

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    # name property with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 chars")
        self._name = value

    # returns all orders for this customer
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    # returns unique coffees ordered
    def coffees(self):
        return list({order.coffee for order in self.orders()})

    # helper to create an order
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Customer who spent the most on a given coffee"""
        spenders = {}
        for order in Order.all:
            if order.coffee == coffee:
                spenders[order.customer] = spenders.get(order.customer, 0) + order.price

        if not spenders:
            return None

        return max(spenders, key=spenders.get)
