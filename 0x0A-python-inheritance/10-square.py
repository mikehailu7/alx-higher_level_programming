#!/usr/bin/python3
# Author: MikiasHailu
# project: square.
""" THis class is the square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is the representation of a square """
    def __init__(self, size):
        """ This function will initialize a square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" This function will returns the area of the square"""
        return self.__size ** 2
