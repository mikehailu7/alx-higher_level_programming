#!/usr/bin/python3
# Author: mikiasHialu
# Area of a square
""" This is square class. """
class Square:
    """ A function with paramter size """
    def __init__(self, size=0):
        """
        paramter:
            size: is a paramter with represents the size of the side.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
    def area(self):
        """
        A function that will find the area of a square
        Returns:
            it will return their area.
        """
        return self.__size ** 2
