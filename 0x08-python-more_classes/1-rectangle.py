#!/usr/bin/python3
"""Defines an empty class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle.
    
    Atrributes:
        width:weidth of the regtangle
        height:height of the regtangle
    """
    def __init__(self, width = 0, height = 0):
         """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.widht = widht
        self.height = height
    @property
    def width(self):
         """Width retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width
    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the height of the regtengle.
        """
        return self.__height
    @width.setter
    def width(self, new_width):
        """Property setter for width of rectangle.

        Args:
            new_width:the new width

        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than 0
        """
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        elif new_width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = new_width
    @height.setter
    def height(self, new_height):
        """Property setter for height of rectangle.

        Args:
            new_height:the new height

        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than 0
        """
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        elif new_height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = new_height
