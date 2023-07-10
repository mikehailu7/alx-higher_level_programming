#!/usr/bin/python3
#Author: MIkiasHailu
#Project: Square
""" This is the square class """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ This is the declaration of a square class """
    def __init__(self, size):
        """ This fucntion is the initialization of the abouve class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" This function will returns the area of the square"""
        return self.__size ** 2
