#!/usr/bin/python3a
# Author: mikiasHailu
# Fun: RectangleTwo

""" This class shows a Rectangle """


class Rectangle:
    """ This will represent a rectangle """
    def __init__(self, width=0, height=0):
        """ This function will Initializes the rectangle """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ This function will describe the width """
        return self.__height

    @height.setter
    def height(self, value):
        """ This function will initialze the attributes for the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ This function will describe the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ This function will initialze the attributes for the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
