#! /usr/bin/python
from lib.interface import Interface
import os.path

APP_ROOT  = os.path.dirname(os.path.realpath('launch.py'))
File_name = 'movie.txt'

file_path = "/".join([APP_ROOT,File_name])

a = Interface(file_path)

a.launch()