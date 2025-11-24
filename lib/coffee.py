from order import Order

class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Coffee name must be a string")
        if len(value) < 3:
            raise Exception("Coffee name must be 3+ characters")
        self._name = value

    # all orders for this coffee
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    # all unique customers
    def customers(self):
        return list({order.customer for order in self.orders()})

    # total orders
    def num_orders(self):
        return len(self.orders())

    # average price paid
    def average_price(self):
        orders = self.orders()
        if not orders:
            return None
        return sum(order.price for order in orders) / len(orders)