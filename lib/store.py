#! /usr/bin/python

import os.path

class Store:
	file_name = None

	@classmethod
	def set_file(cls,file_name):
		cls.file_name = file_name

	@classmethod
	def is_usable(cls):
		return os.path.exists(cls.file_name)

	@classmethod
	def create_file(cls):
		file = open(cls.file_name, 'w')
		file.close
		return True

	
	@classmethod
	def write_into_file(cls,args):
		args = ("\t").join(args)
		file = open(cls.file_name, 'a')
		file.write(args + "\n" )
		file.close
		return True

	@classmethod
	def read_data_from_file(cls):
		data = []
		file = open(cls.file_name, 'r')
		for line in file:
			data.append(line.strip().split("\t"))
		file.close
		return data
		