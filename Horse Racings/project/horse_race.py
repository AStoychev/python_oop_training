class HorseRace:
    __VALID_TYPE_RACE = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in self.__VALID_TYPE_RACE:
            raise ValueError('Race type does not exist!')
        self.__race_type = value

