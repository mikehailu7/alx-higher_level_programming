#!/usr/bin/python3
# Author: MikiasHailu
# Project: FullRectangle
""" This module contains the Rectangle and BaseGeometery """


class BaseGeometry:
    """ This class is the representation of base geometery """

    def area(self):
        """ This function will calculate the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ THis function is for validation """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ This is a rectangle class """

    def __init__(self, width, height):
        """ This fucntion is there for initalizaion """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ THis function will calcualte the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ THis fucntion is the representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
