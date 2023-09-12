from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    __MAX_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.__MAX_SPEED:
            raise ValueError('Horse speed is too high!')
        self.__speed = value

    def train(self):
        if self.speed + 2 > self.__MAX_SPEED:
            self.speed = self.__MAX_SPEED
        else:
            self.speed += 2
