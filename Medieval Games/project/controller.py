class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __take_last_supply(self, supply_type):
        for i in range(len(self.supplies) -1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
            if supply_type == 'Food':
                raise Exception('There are no food supplies left!')
            if supply_type == 'Drink':
                raise Exception('There are no drink supplies left!')

    def __find_player_by_name(self, name):
        for p in self.players:
            if p.name == name:
                return p

    @staticmethod
    def __check_of_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f'Player {player.name} does not have enough stamina.')
        if result:
            return  '\n'.join(result)

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)

        if p1 < p2:
            return f'Winner: {p2.name}'
        else:
            return f'Winner: {p1.name}'

    def add_player(self, *args):
        successful_added_name = []
        for i in args:
            if i not in self.players:
                self.players.append(i)
                successful_added_name.append(i.name)
        return f"Successfully added: {', '.join(successful_added_name)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player_by_name(player_name)
        if player.stamina == 100:
            return f'{player_name} have enough stamina.'

        supply = self.__take_last_supply(sustenance_type)
        if supply:
            player._sustain_player(supply)
            return f'"{player_name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name, second_player_name):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_of_the_players_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player < second_player:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)

        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result
