#! /usr/bin/python

import sys
sys.path.insert(0, '/home/salman-vpc/python/Python-OOP')

from lib.store import Store
import unittest

class testing_SoterClass(unittest.TestCase):

	global file_path
	file_path = "/home/salman-vpc/python/Python-OOP/movie.txt"

	def test_class_variable_file(self):
		Store.set_file(file_path)
		self.assertEqual(file_path,Store.file_name) 

	def test_is_the_file_usable(self):
		Store.set_file(file_path)
		self.assertTrue(Store.is_usable())

	def test_write_into_the_file(self):
		args = ["Iron Man3", "2013", "8.5"]
		self.assertTrue(Store.write_into_file(args))

	def test_read_data_from_file(self):
		Store.set_file(file_path)
		a = ["Iron Man3", "2013", "8.5"]
		b = Store.read_data_from_file()[0]
		self.assertListEqual(a, b)

	def test_create_file(self):
		Store.set_file(file_path)
		self.assertTrue(Store.create_file)



suite = unittest.TestLoader().loadTestsFromTestCase(testing_SoterClass)
unittest.TextTestRunner(verbosity=2).run(suite)