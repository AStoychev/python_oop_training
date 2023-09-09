from project.movie_specification.movie import Movie


class Action(Movie):
    __AGE_RESTRICTION_MESSAGE = 'Action movies must be restricted for audience under 12 years!'

    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @classmethod
    def __validate_age_restriction(cls, age):
        if age < 12:
            raise ValueError(cls.__AGE_RESTRICTION_MESSAGE)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        self.__validate_age_restriction(value)
        self.__age_restriction = value

    def details(self):
        return f'Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, ' \
               f'Likes:{self.likes}, Owned by:{self.owner.username}'
