from astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    def find_astronaut_for_mission(self, count, min_oxygen):
        return sorted([x for x in self.astronauts if x.oxigen > min_oxygen],
                      key=lambda x: x.oxigen,
                      reverse=True)[0:count]


