from abc import ABC, abstractmethod

from project.utils import is_positive


class Table(ABC):
    # If use one way to set value you have to remove this class attributes
    _MIN_TABLE_NUMBER = None
    _MAX_TABLE_NUMBER = None
    _INVALID_TABLE_NUMBER_MESSAGE = None

    __INVALID_CAPACITY_MESSAGE = "Capacity has to be greater than 0!"

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

        self.__initialize()

    def __initialize(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if self.is_reserved:
            return None

        return f'''
Table: {self.table_number}
Type: {self.table_type}
Capacity: {self.capacity}
        '''

    @property
    @abstractmethod
    def table_type(self):
        pass

    # Оne way to force inheritors to add values
    # @abstractmethod
    # @property
    # def MIN_TABLE_NUMBER(self):
    #     pass
    #
    # @abstractmethod
    # @property
    # def MAX_TABLE_NUMBER(self):
    #     pass
    #
    # @abstractmethod
    # @property
    # def INVALID_TABLE_NUMBER_MESSAGE(self):
    #     pass

    @classmethod
    def __validate_capacity(cls, value):
        if not is_positive(value):
            raise ValueError(cls.__INVALID_CAPACITY_MESSAGE)

    @classmethod
    def __validate_table_number(cls, value):
        if cls._MIN_TABLE_NUMBER and value < cls._MIN_TABLE_NUMBER:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)
        if cls._MAX_TABLE_NUMBER and cls._MAX_TABLE_NUMBER < value:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, food):
        self.food_orders.append(food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) +\
               sum(d.price for d in self.drink_orders)

    def clear(self):
        self.__initialize()
    
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self.__capacity = value

    # Other way to force inheritors to add value
    @property
    def table_number(self):
        return self.__table_number
    
    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self.__table_number = value
