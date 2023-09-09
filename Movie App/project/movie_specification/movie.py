from abc import ABC, abstractmethod


class Movie(ABC):
    __INVALID_TITLE_MESSAGE = 'The title cannot be empty string!'
    __INVALID_YEAR_MESSAGE = 'Movies weren\'t made before 1888!'
    __INVALID_OWNER_MESSAGE = 'The owner must be an object of type User!'

    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @classmethod
    def __validate_title(cls, value):
        if value == "":
            raise ValueError(cls.__INVALID_TITLE_MESSAGE)

    @classmethod
    def __validate_year(cls, year):
        if year < 1888:
            raise ValueError(cls.__INVALID_YEAR_MESSAGE)

    @classmethod
    def __validate_owner(cls, value):
        if not type(value).__name__ == 'User':
            raise ValueError(cls.__INVALID_OWNER_MESSAGE)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__validate_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__validate_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__validate_owner(value)
        self.__owner = value

    @abstractmethod
    def details(self):
        ...
