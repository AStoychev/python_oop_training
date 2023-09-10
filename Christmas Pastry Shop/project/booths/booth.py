from abc import ABC, abstractmethod


class Booth(ABC):
    __CAPACITY_ERROR_MESSAGE = 'Capacity cannot be a negative number!'

    @abstractmethod
    def __init__(self, booth_number, capacity):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @classmethod
    def __validate_capacity(cls, value):
        if value < 0:
            raise ValueError(cls.__CAPACITY_ERROR_MESSAGE)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self.__capacity = value

    def get_bill(self):
        return self.price_for_reservation + sum([d for d in self.delicacy_orders])

    @abstractmethod
    def reserve(self, number_of_people):
        pass
