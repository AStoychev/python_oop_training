class User:
    __INVALID_USERNAME_MESSAGE = 'Invalid username!'
    __INVALID_AGE_MESSAGE = 'Users under the age of 6 are not allowed!'

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @classmethod
    def __validate_username(cls, value):
        if value == "":
            raise ValueError(cls.__INVALID_USERNAME_MESSAGE)

    @classmethod
    def __validate_age(cls, age):
        if age < 6:
            raise ValueError(cls.__INVALID_AGE_MESSAGE)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def __str__(self):
        final_result = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']

        if len(self.movies_liked) > 0:
            for liked in self.movies_liked:
                final_result.append(liked.details())
        else:
            final_result.append('No movies liked.')

        final_result.append('Owned movies:')
        if len(self.movies_owned) > 0:
            for owned in self.movies_owned:
                final_result.append(owned.details())
        else:
            final_result.append('No movies owned.')

        return '\n'.join(final_result)
