class Order:
  #class variable to store all orders
    orders = []

    def __init__(self,customer,coffee,price):
     self.customer =customer
     self.coffee =coffee
     self.price =price

     #add this order to the list of orders
     Order.orders.append(self)

     @property
     def customer(self):
        return self ._customer

     @customer .setter
     def customer(self,value):
        if not isinstance(value, str):
            raise TypeError("customer must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("customer name must be 1–15 characters long")

            self._customer

     @property
     def coffee(self):
          return self ._coffee

     @name.setter
     def name(self, value):
        if not isinstance(value, str):
            print("Coffee name must be a string.")
        if len(value) < 3:
            raise TypeError("Coffee name must be at least 3 characters long")

        self ._coffee = value

        @property
        def price(self):
          return self ._price

     @price .setter
     def price(self,value):
        self ._price = value
        if not isinstance(value,float):
           print('price must be a float')
        if not(1.0<=value<=10.0):
           raise TypeError('price must be between 1.0 and 10.0')
        self ._customer = value









    