#!/usr/bin/python3
# Author: MikiasHailu
# Project: Integer validator
""" This class is a BaseGeometry class """

class BaseGeometry:
    """ This class is called th base geometry class """
    def area(self):
        """ This function wil raises an exception when it is called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function will validate the integer value. """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
