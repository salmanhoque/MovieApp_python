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
			user_action = raw_input("\n\nWhat you wanna do? cmd --> add, list, find or quit\n >").strip()
			user_action = user_action.split(" ")
			action      = self.actions(user_action)
		self.ending_mgs()


	def actions(self,user_action):
		action = user_action.pop(0).lower()

		if action == 'add':
			self.add()
		elif action == 'list':
			self.list_movie(user_action)
		elif action == 'find':
			self.find_movie(user_action)	
		elif action == 'quit':
			return 'quit'


	def add(self):
		args = []
		self.header_output("Adding....")
		args.append(raw_input("Enter Movie Name: ").strip())
		args.append(raw_input("Enter Release year: ").strip())
		args.append(raw_input("Enter Movie Rating: ").strip())
		if Movie.add_movie_into_file(args):
			print("\nNew movie has been added to your movie list")
		else:
			print("\nSorry File Error!")
		

	def list_movie(self,kwargs):
		print "\n Example: list name, list rating, list date or list by name etc. \n"
		sort_order = 'name'
		if kwargs != []:
			if kwargs[0] == 'by':
				sort_order = kwargs.pop(1)
			else: 
				sort_order = kwargs.pop(0)
		
		movies = Movie.read_movies_from_file()
		if sort_order == 'date':
			movies.sort(cmp = lambda x, y: cmp(x.date, y.date))
		elif sort_order == 'rating':
			movies.sort(cmp = lambda x, y: cmp(x.rating, y.rating))			
		else:
			movies.sort(cmp = lambda x, y: cmp(x.movie, y.movie))
		self.movie_table_output(movies)


	def find_movie(self,user_action):
		self.header_output("Finding....")
		print "\n Example: find iron or find Iron Man 3 \n"
		movies = Movie.read_movies_from_file()
		if user_action != []:
			arg    = user_action.pop(0)
			found  = [x for x in movies if self.search(x,arg)]
			self.movie_table_output(found)

    	print "\n Example: find iron or find Iron Man 3 \n"

	def search(self,x,arg):
		movie_names = x.movie.split(" ")
		found = [x for x in movie_names if x.lower() == arg.lower()]
		return found

	def welcome_msg(self):
		self.header_output("Welcome To Python Movie App") 

	def ending_mgs(self):
		self.header_output("<<< GoodBye! >>>")
		print "\n\n"
	

	def header_output(self,text):
		print text.center(80)

	def movie_table_output(self,movies):
		print "="*80
		print "Movie Name".ljust(40) + "Release Year".ljust(25) + "Rating".rjust(15)
		print "="*80
		for movie in movies:
			print movie.movie.ljust(40) + movie.date.ljust(25) + movie.rating.rjust(15) 
		print "="*80

