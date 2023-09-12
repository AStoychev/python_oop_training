from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorsesFactory:
    @staticmethod
    def create_horse(horse_type, horse_name, horse_speed):
        if horse_type == 'Appaloosa':
            return Appaloosa(horse_name, horse_speed)
        elif horse_type == 'Thoroughbred':
            return Thoroughbred(horse_name, horse_speed)


class JockeyFactory:
    @staticmethod
    def create_jockey(jockey_name, age):
        return Jockey(jockey_name, age)


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def check_if_horse_already_add(self, name):
        for horse in self.horses:
            if horse.name == name:
                return True
        return False

    def check_if_jockey_already_add(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return True
        return False

    def check_if_race_type_already_exist(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return True
        return False

    def check_jockey_have_horse(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                if jockey.horse:
                    return True
        return False

    def check_for_available_horse(self, horse_type):
        for horse in reversed(self.horses):
            if not horse.__class__.__name__ == horse_type:
                pass
            else:
                if horse.is_taken:
                    pass
                else:
                    return horse

    @staticmethod
    def check_jockey_is_already_in_race_list(name, jockeys):
        for jockey in jockeys:
            if jockey.name == name:
                return True
        return False

    def find_jockey(self, jockey_name_):
        found_jockey = next(filter(lambda x: x.name == jockey_name_, self.jockeys), None)
        if found_jockey:
            return found_jockey

    def find_horse_race(self, race_type_):
        found_race = next(filter(lambda x: x.race_type == race_type_, self.horse_races), None)
        if not found_race:
            raise Exception(f"Race {race_type_} could not be found!")
        return found_race

    def add_horse(self, horse_type, horse_name, horse_speed):
        if self.check_if_horse_already_add(horse_name):
            raise Exception(f'Horse {horse_name} has been already added!')

        horse = HorsesFactory().create_horse(horse_type, horse_name, horse_speed)
        self.horses.append(horse)
        return f'"{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name, age):
        if self.check_if_jockey_already_add(jockey_name):
            raise Exception(f'Jockey {jockey_name} has been already added!')

        jockey = JockeyFactory.create_jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type):
        if self.check_if_race_type_already_exist(race_type):
            raise Exception(f'Race {race_type} has been already created!')

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name, horse_type):
        if not self.check_if_jockey_already_add(jockey_name):
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if self.check_jockey_have_horse(jockey_name):
            return f'Jockey {jockey_name} already has a horse.'

        if not self.check_for_available_horse(horse_type):
            raise f'Horse breed {horse_type} could not be found!'
        else:
            for jockey in self.jockeys:
                if jockey.name == jockey_name:
                    horse = self.check_for_available_horse(horse_type)
                    jockey.horse = horse
                    return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        race = self.find_horse_race(race_type)
        jockey = self.find_jockey(jockey_name)

        if not self.check_if_jockey_already_add(jockey_name):
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if jockey in race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'
        else:
            race.jockeys.append(jockey)
            return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type):
        race = self.find_horse_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        faster_jockey = sorted(race.jockeys, key=lambda jockeys: -jockeys.horse.speed)[0]
        return f'The winner of the {race_type} race, with a speed of {faster_jockey.horse.speed}km/h is ' \
               f'{faster_jockey.name}! Winner\'s horse: {faster_jockey.horse.name}.'
