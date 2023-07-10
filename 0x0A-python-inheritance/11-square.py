#!/usr/bin/python3
# Author: MikiasHailu
# Project: Square
""" This module contains basegeometery rectangle and square classes """


class BaseGeometry:
    """ This is the base Geometry class """
    def area(self):
        """ This function will raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This fucntion is for validating """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ This class is a rectangle class """
    def __init__(self, width, height):
        """ This fucntion is for initalization of the rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ This function will calculate the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ This fucntion is the representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """ This class is a square rectangle class """
    def __init__(self, size):
        """ This fucntion is for initalization of the square rectangle """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ This function will calculate the area of the rectangle """
        return self.__size ** 2

    def __str__(self):
        """ This fucntion is the representation of the square rectangle """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
