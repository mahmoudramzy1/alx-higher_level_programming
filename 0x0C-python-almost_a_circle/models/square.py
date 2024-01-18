#!/usr/bin/python3
"""module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """retruns string info about the square object"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
