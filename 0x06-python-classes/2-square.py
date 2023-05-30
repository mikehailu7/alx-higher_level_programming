#!/usr/bin/python3
# Author: MikiasHailu
# Size validation
""" this is a square class. """
class Square:
    """ a function that initalize the square with parameters. """
    def __init__(self, size=0):
        """
        Parameter:
            size: is a paramter that represents the size.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
