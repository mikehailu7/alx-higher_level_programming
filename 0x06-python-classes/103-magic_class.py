#!/usr/bin/python3
# Author: mikiasHailu
# ByteCode
"""This will declare Class"""
import math
class MagicClass:
    """This represents a circle"""
    def __init__(self, radius=0):
        """ This functionw have a paramter of radius the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    def area(self):
        """ This fucntion  will Calculaes the area of the circle
        Returns:
            This will return The area of the square
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle
        Returns:
            returns the cirumference of the circle.
        """
        return 2 * math.pi * self.__radius
