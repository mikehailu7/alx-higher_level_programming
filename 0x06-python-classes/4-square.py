#!/usr/bin/python3
# Author: MikiasHailu
# Access and update private attribute
"""THis is a class square."""
class Square:
    """This is a sqare class."""
    def __init__(self, size=0):
        """A funtion that reperesents a square.
        paramter:
            size: This paratmeter represents the size of the side.
        """
        self.size = size
    @property
    def size(self):
        """represents the sides
        Returns:
            This will return The size of the side.
        """
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size) ** 2
