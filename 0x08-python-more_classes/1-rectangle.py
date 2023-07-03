#!/usr/bin/python3
# Author: MikiasHailu
# Fun: rectangletwo

""" This is a rectangle class """

class Rectangle:
    """this functoin shows a rectangle"""
    def __init__(self, width=0, height=0):
        """This is the declaration of rectangle"""
        self.height = height
        self.width = width


   @property
    def height(self):
        """this funciton shows the height attribute of the rectangle"""
        return self.__height


    @height.setter
    def height(self, value):
        """This function will set instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    @property
    def width(self):
        """this is a fucntion for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this function shows  attribute of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
