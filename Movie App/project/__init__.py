from project.movie_app import MovieApp
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User

# user = User('', 18)
# movie = Fantasy('Indiana', 1994, 'Sean', 6)
# print(movie.details())

# movie_app = MovieApp()
# print(movie_app.register_user('Pesho', 18))
# print(movie_app.register_user('Pesho', 18))

movie_app = MovieApp()
print(movie_app.register_user('Pesho', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Pesho', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Pesho', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Pesho', movie2))
print(movie_app.like_movie('Pesho', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)
# print(movie_app.delete_movie('Alexandra', movie2))
# print(movie_app.delete_movie('Pesho', movie))
print('------------------------------')