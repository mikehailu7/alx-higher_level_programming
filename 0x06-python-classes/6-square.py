#!/usr/bin/python3
# Author: MikiasHailu
# Printing a square
"""THis is a class square"""
class Square:
    """ Represents a square
    Attributes:
        size: This is a paramter that represents size of the side.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ This function will represents square with a size and position.
        Paramter:
            position: This paramter represents the position of the new square.
            size: This paramter represents the size of the a square.
        Returns:
            returns the current size and positon.
        """
        self.size = size
        self.position = position
    @property
    def size(self):
        """ This function represents the current size of the square."""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """ This function will get the current position of the square.
        Returns:
            It returns the current position.
        """
        return (self.__position)
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """ This fucntion will calcualte area of the square.
        Returns:
            The area of the square.
        """
        return (self.__size) ** 2
    def my_print(self):
        """ Print the square with the character."""
        if self.__size == 0:
            print("")
            return

        [print("") for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")
