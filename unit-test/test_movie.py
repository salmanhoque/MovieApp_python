#! /usr/bin/python

import sys
sys.path.insert(0, '/home/salman-vpc/python/Python-OOP')

from lib.movie import Movie
from lib.store import Store
import unittest

class testing_MovieClass(unittest.TestCase):
	global file_path
	file_path = "/home/salman-vpc/python/Python-OOP/movie.txt"

	def test_has_init_method(self):
		a = Movie("Iron Man3", "2013", "8.5")
		self.assertIsInstance(a, Movie)

	def test_accessors_value(self):
		a = Movie("Iron Man3", "2013", "8.5")
		self.assertEqual("Iron Man3", a.get_movie() )
		self.assertEqual("2013",	  a.get_date()  )
		self.assertEqual("8.5", 	  a.get_rating())
	
	def test_add_movie_into_file(self):
		Store.set_file(file_path)
		args = ["Super Man", "2013", "8.5"]
		self.assertTrue(Movie.add_movie_into_file(args))
	

	def test_read_movies_from_file(self):
		Store.set_file(file_path)
		a = Movie.read_movies_from_file()[0]
		self.assertIsInstance(a, Movie)

suite = unittest.TestLoader().loadTestsFromTestCase(testing_MovieClass)
unittest.TextTestRunner(verbosity=2).run(suite)