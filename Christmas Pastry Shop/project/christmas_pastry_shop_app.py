from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class DelicacyFactory:
    @staticmethod
    def create(type_delicacy, name, price):
        if type_delicacy == 'Gingerbread':
            return Gingerbread(name, price)
        elif type_delicacy == 'Stolen':
            return Stolen(name, price)
        else:
            return None


class BoothFactory:
    @staticmethod
    def create(type_booth, booth_number, capacity):
        if type_booth == 'Open Booth':
            return OpenBooth(booth_number, capacity)
        elif type_booth == 'Private Booth':
            return PrivateBooth(booth_number, capacity)
        else:
            return None


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0
        self.final_income = []

    def check_if_delicacy_exist(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return True
        return False

    def check_if_number_exist(self, number):
        for numbers in self.booths:
            if numbers.booth_number == number:
                return True
        return False

    def add_delicacy(self, type_delicacy, name, price):
        if self.check_if_delicacy_exist(name):
            raise Exception(f'{name} already exists!')

        delicacy = DelicacyFactory().create(type_delicacy, name, price)
        if not delicacy:
            raise Exception(f'{type_delicacy} is not a valid booth!')
        else:
            self.delicacies.append(delicacy)
            return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth, booth_number, capacity):
        if self.check_if_number_exist(booth_number):
            raise Exception(f'Booth number {booth_number} already exists!')

        booth = BoothFactory().create(type_booth, booth_number, capacity)
        if not booth:
            raise Exception(f'{type_booth} is not a valid booth!')
        else:
            self.booths.append(booth)
            return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people):
        for booth in self.booths:
            if booth.is_reserved or booth.capacity < number_of_people:
                raise Exception(f'No available booth for {number_of_people} people!')
            else:
                booth.is_reserved = True
                booth.reserve(number_of_people)
                return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number, delicacy_name):
        if not self.check_if_number_exist(booth_number):
            raise Exception(f'Could not find booth {booth_number}!')
        elif not self.check_if_delicacy_exist(delicacy_name):
            raise Exception(f'No {delicacy_name} in the pastry shop!')
        else:
            for booth in self.booths:
                for delicacy in self.delicacies:
                    if booth.booth_number == booth_number:
                        if delicacy.name == delicacy_name:
                            booth.delicacy_orders.append(delicacy.price)
            return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                self.income = booth.get_bill()
                self.final_income.append(self.income)
                booth.delicacy_orders = []
                booth.price_for_reservation = 0
                booth.is_reserved = False
                return f'Booth {booth_number}: \n' \
                       f'Bill: {self.income:.2f}lv.'

    def get_income(self):
        all_income = sum(self.final_income)
        return f'Income: {all_income:.2f}lv.'
