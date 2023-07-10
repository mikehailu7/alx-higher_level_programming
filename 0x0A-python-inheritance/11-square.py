#!/usr/bin/python3
#Author: MikiasHailu
#Project: Full rectangle
""" This module contains the Rectangle BaseGeometry class and square class """

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
    """ THis class is base geomery class. """
    def area(self):
        """ This is an area function with exception. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function will check the height"""
        self.integer_validator("height", height)
        self.__height = height

     def __str__(self):
         """ This fucntion is informal string representation of a rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """ this class is the square class """
    def __init__(self, size):
        """ This function is the initialization of the square rectangle """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" This function will returns the area of the square rectangle """
        return self.__size ** 2

    def __str__(self):
        """ This fucntion is informal string representation of the square rectangle """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
