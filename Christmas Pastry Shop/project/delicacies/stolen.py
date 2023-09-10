from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    __DEFAULT_PORTION = 250

    def __init__(self, name, price):
        super().__init__(name, self.__DEFAULT_PORTION, price)

    def details(self):
        return f'Stolen {self.name}: 250g - {self.price:.2f}lv.'
