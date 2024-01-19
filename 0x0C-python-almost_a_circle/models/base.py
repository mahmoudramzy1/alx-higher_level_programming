#!/usr/bin/python3
"""this is the circle module"""
from json import dumps, loads


class Base:
    """this is the base class"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Jsonifies a dictionary so it's quite rightly and longer."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
