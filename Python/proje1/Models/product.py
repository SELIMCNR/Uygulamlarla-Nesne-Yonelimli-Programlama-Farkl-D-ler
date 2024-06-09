class Product:
    def __init__(self, name="Default", price=0, quantity=1):
        print(f"An instance with name : {name} has been derived from Product class")
        self.__name = name  # __name is a private attribute
        self.__price = price  # __price is a private attribute
        self.__quantity = quantity  # __quantity is a private attribute

    # encapsulation
    @property  # getter
    def name(self):
        return self.__name

    @name.setter  # setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def get_total_price(self):
        return self.__price * self.__quantity

    def __repr__(self):
        return f"Product({self.__name}, {self.__price}, {self.__quantity})"
