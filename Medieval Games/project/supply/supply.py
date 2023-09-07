from abc import ABC, abstractmethod


class Supply(ABC):
    __EMPTY_NAME_MESSAGE = 'Name cannot be an empty string.'
    __NEGATIVE_ENERGY_MESSAGE = 'Energy cannot be less than zero.'

    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @classmethod
    def __check_for_empty_string_or_whitespace(cls, value):
        if not value or not value.strip():
            raise ValueError(cls.__EMPTY_NAME_MESSAGE)

    @classmethod
    def __check_for_negative_number(cls, value):
        if value < 0:
            raise ValueError(cls.__NEGATIVE_ENERGY_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__check_for_empty_string_or_whitespace(value)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__check_for_negative_number(value)
        self.__energy = value

    @abstractmethod
    def details(self):
        pass
