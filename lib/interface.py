#! /usr/bin/python

from movie import Movie
from store import Store

class Interface:
	
	def __init__(self, file_path):
		if Store.is_usable:
			Store.file_name = file_path
			print "\nFound Your File!\n\n"
		else:
			Store.file_name = file_path
			Store.create_file()
			print "Your file has been created!\n\n"
		
	def launch(self):	
		self.welcome_msg()
		action = None

		while action != "quit":
			user_action = raw_input("\n\nWhat you wanna do? cmd --> add, list, find\n >").strip()
			action      = self.actions(user_action)
		self.ending_mgs()


	def actions(self,user_action):
	    if user_action =='add':
	    	self.add()
	    elif user_action == 'list':
	    	self.list_movie()
	    elif user_action == 'find':
	    	self.find_movie()
	    elif user_action == 'quit':
	    	return 'quit'

	def add(self):
		self.header_output("Adding....")

	def list_movie(self):
		movies = Movie.read_movies_from_file()
		self.movie_table_output(movies)

	def find_movie(self):
		self.header_output("Findding....")


        	
	def welcome_msg(self):
		self.header_output("Welcome To Python Movie App") 

	def ending_mgs(self):
		self.header_output("<<< GoodBye! >>>")
		print "\n\n"
	

	def header_output(self,text):
		print text.center(80)

	def movie_table_output(self,movies):
		self.header_output("All Movie List")
		print "="*80
		print "Movie Name".ljust(40) + "Release Year".ljust(25) + "Rating".rjust(15)
		print "="*80
		for movie in movies:
			print movie.movie.ljust(40) + movie.date.ljust(25) + movie.rating.rjust(15) 
		print "="*80

