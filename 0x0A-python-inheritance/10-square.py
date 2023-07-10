#!/usr/bin/python3
# Author: MikiasHailu
# Project: Square
""" This is a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class Represent a square """

    def __init__(self, size):
        """ This function will Initialize a new square.
        Arguments:
            size: This is the size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
