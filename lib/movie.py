
from store import Store

class Movie:

	@classmethod
	def add_movie_into_file(cls,args):
		return Store.write_into_file(args)
		
	@classmethod
	def read_movies_from_file(cls):
		movie_list = []
		movies = Store.read_data_from_file()
		for movie in movies:
			movie_list.append(Movie(movie[0],movie[1],movie[2]))
		return movie_list


	
	def __init__(self,movie,date,rating):
		self.movie  = movie
		self.date   = date
		self.rating	= rating
		
	def get_movie(self):
		return self.movie

	def get_date(self):
		return self.date

	def get_rating(self):
		return self.rating