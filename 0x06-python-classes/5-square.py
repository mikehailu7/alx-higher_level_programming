#!/usr/bin/python3
# Author: MikiasHailu
# Printing a square
"""THis is a class square"""
class Square:
    """ Represents a square
    Attributes:
        size: This is a paramter that represents size of the side.
    """
    def __init__(self, size=0):
        """ function with a paramter size of the square.
        paramter:
            size: This is a paramter with size of a side.
        Returns:
            this will return None
        """
        self.size = size
    def area(self):
        """ This function will calculate the area.
        Returns:
            And also returns The area of the square.
        """
        return (self.__size) ** 2
    @property
    def size(self):
        """ This function is to get the size
        Returns:
            it will return size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """ This function will set the size with paratmeter size and value.
        paramter:
            value: the value of the side.
        Returns:
            This will return None.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    def my_print(self):
        """ this function will print the squre.
        Returns:
            will retrun None.
        """
        if self.__size == 0:
            print()
            return
        for m in range(self.__size):
            print("".join(["#" for n in range(self.__size)]))
