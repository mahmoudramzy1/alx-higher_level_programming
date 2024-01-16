#!/usr/bin/python3
"""this is the circle module"""


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
