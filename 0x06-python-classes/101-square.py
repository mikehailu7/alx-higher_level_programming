#!/usr/bin/python3
# Author: MikiasHailu
# Print Square instance

"""This is a class declaration."""
class Square:
    """ THis is a class called square."""

    def __init__(self, size=0, position=(0, 0)):
        """This is a function with size and position paramters.
        paramter:
            position: This shows the squares position.
            size: This shows the square size
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """THis function will represent the size of the square.
        Return:
            This returns the size.
        """
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
        """THis function will represent the positon of the square.
        Return:
            This returns the position.
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
    def my_print(self):
        """THis function will print the size of the square.
        Return:
            This will none.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")    
    def area(self):
        """THis function will represent the area of the square.
        Return:
            This returns the area.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """THis function will represent the str.
        Return:
            This returns none.
        """
        if self.__size != 0:
            [print("") for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            if m != self.__size - 1:
                print("")
        return ("")
