from project.client import Client


class FoodOrdersApp:
    bill_number = 0

    def __init__(self):
        self.menu = []
        self.client_list = []

    def __get_client(self, client_phone_number_):
        # find_client = next(filter(lambda x: x.phone_number == client_phone_number_, self.client_list), None)
        for client in self.client_list:
            if client.phone_number == client_phone_number_:
                return client

    def __find_client(self, client_phone_number_):
        for client in self.client_list:
            if client.phone_number == client_phone_number_:
                return client

    def register_client(self, client_phone_number):
        client = self.__get_client(client_phone_number)

        if client:
            raise Exception(f'The client has already been registered!')

        client = Client(client_phone_number)
        self.client_list.append(client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals):
        list_of_meals = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if type(meal).__name__ in list_of_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        all_meal = []
        for meal in self.menu:
            all_meal.append(meal.details())
        return '\n'.join(all_meal)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_name):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        if not self.__get_client(client_phone_number):
            self.register_client(client_phone_number)

        client = self.__find_client(client_phone_number)
        client_bill = 0
        all_meals = []

        for k, v in meal_name.items():
            for meal in self.menu:
                if meal.name == k:
                    if meal.quantity >= v:
                        all_meals.append(meal)
                        client_bill += v * meal.price
                        break
                    else:
                        raise Exception(f'Not enough quantity of {meal.__class__.__name__}: {k}!')
            else:
                raise Exception(f'{k} is not on the menu!')

        client.shopping_cart.extend(all_meals)
        client.bill += client_bill

        for k, v in meal_name.items():
            if k not in client.ordered_meal:
                client.ordered_meal[k] = 0
            client.ordered_meal[k] += v
            for meal in self.menu:
                if meal.name == k:
                    meal.quantity -= v

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)}" \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.__find_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception('There are no ordered meals!')

        for k, v in client.ordered_meal.items():
            for meal in self.menu:
                if k == meal.name:
                    meal.quantity += v

        client.shopping_cart = []
        client.bill = 0
        client.ordered_meal = {}
        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number):
        client = self.__find_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception('There are no ordered meals!')

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meal = {}
        self.bill_number += 1
        return f'Receipt #{self.bill_number} with total amount of {total_paid_money:.2f} was successfully paid for ' \
               f'{client_phone_number}.'

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.client_list)} clients.'