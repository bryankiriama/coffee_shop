
class Coffee:
    def __init__(self,name):
        self.name =name

        @property
        def name(self):
          return self ._coffee

        @name.setter
        def name(self, value):
         if not isinstance(value, str):
            print("Coffee name must be a string.")
         if len(value) < 3:
            raise TypeError("Coffee name must be at least 3 characters long")
         self._name = value
