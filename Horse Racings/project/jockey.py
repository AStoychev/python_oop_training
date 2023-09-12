class Jockey:
    __INVALID_NAME_MESSAGE = 'Name should contain at least one character!'
    __INVALID_AGE_MESSAGE = 'Jockeys must be at least 18 to participate in the race!'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.horse = None

    @classmethod
    def __validate_name(cls, name):
        if name.strip() == "":
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_age(cls, age):
        if age < 18:
            raise ValueError(cls.__INVALID_AGE_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
