#!/usr/bin/python3
# Author: Mikiashailu
# fun: Print_square
"""
This module is print_square
The module will print the squre size).
"""
def print_square(size):
    """This function will prints a square's size"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
