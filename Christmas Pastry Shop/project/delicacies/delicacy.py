from abc import ABC, abstractmethod


class Delicacy(ABC):
    __INVALID_NAME_MESSAGE = 'Name cannot be null or whitespace!'
    __INVALID_PRICE_MESSAGE = 'Price cannot be less or equal to zero!'

    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @classmethod
    def __validate_name(cls, value):
        if not value or not value.strip():
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_price(cls, price):
        if price <= 0:
            raise ValueError(cls.__INVALID_PRICE_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    @abstractmethod
    def details(self):
        pass
