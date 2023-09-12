from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    __MAX_SPEED = 140

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
        if self.speed + 3 > self.__MAX_SPEED:
            self.speed = self.__MAX_SPEED
        else:
            self.speed += 3
