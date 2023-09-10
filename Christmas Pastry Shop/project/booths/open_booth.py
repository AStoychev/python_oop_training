from project.booths.booth import Booth


class OpenBooth(Booth):
    __PRICE_FOR_RESERVATION_OPEN_BOOTH = 2.50

    def __init__(self, booth_number, capacity):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * self.__PRICE_FOR_RESERVATION_OPEN_BOOTH
        self.is_reserved = True
