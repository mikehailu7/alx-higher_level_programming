#!/usr/bin/python3
# Author: mikiasHailu
# Fun: rectangleFour

""" This function will define a class Rectangle """


class Rectangle:
    """This function is about a rectangle"""
    def __init__(self, width=0, height=0):
        """This is the declaration of the rectangle"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """This function shows the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this fucntion will set the attribute of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """This function shows the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This fucntion will set the attribute of the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ This fucntion will return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ This fuction will returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ This function will returns printable string of the rectangle """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string = string + "\n".join("#" * self.__width
                    for m in range(self.__height))
            return string
