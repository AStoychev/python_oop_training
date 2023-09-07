from project.supply.supply import Supply


class Player:
    player_name = []
    __INVALID_NAME_MESSAGE = 'Name not valid!'
    __INVALID_AGE_MESSAGE = 'The player cannot be under 12 years old!'
    __INVALID_STAMINA_MESSAGE = 'Stamina not valid!'

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @classmethod
    def __validate_name(cls, value):
        if value == "":
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @staticmethod
    def __check_name_already_exist(cls, value):
        if value in Player.player_name:
            raise Exception(f'Name {value} is already used!')

    @classmethod
    def __validate_age(cls, value):
        if value < 12:
            raise ValueError(cls.__INVALID_AGE_MESSAGE)

    @classmethod
    def __validate_stamina(cls, value):
        if not 0 <= value <= 100:
            raise ValueError(cls.__INVALID_STAMINA_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        Player.player_name.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__validate_stamina(value)
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def _sustain_player(self, supply: Supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy

    def __lt__(self, other):
        return self.stamina < other.stamina

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'