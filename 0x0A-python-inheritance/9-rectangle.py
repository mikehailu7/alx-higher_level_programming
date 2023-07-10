#!/usr/bin/python3
# Author: MikiasHailu
# Project: Full rectangle
""" This module contains the Rectangle and BaseGeometry class """

class Rectangle(BaseGeometry):
    """ This is a rectangle class """

    def __init__(self, width, height):
        """ This function is the initialization of the rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ This function is informal string representation of a rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """ This function will calculate the area of the rectangle """
        return self.__width * self.__height


class BaseGeometry:
    """ THis class is base geomery class """

    def area(self):
        """ This is an area function with exception. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function will check that value is an integer greater than 0 """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
