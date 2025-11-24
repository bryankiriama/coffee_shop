class Order:
    all = []

    def __init__(self, customer, coffee, price):
        # customer must be Customer instance
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise Exception("Order must have a valid Customer")

        if not isinstance(coffee, Coffee):
            raise Exception("Order must have a valid Coffee")

        if not (isinstance(price, float) or isinstance(price, int)):
            raise Exception("Price must be a number")
        if not (1.0 <= price <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price