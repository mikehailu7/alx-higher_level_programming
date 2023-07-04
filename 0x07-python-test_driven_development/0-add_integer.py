#!/usr/bin/python3
# Author: mikiasHailu
# fun: Integers addition
"""
This module is the 0-add_integer.
This module will add integer a and b return their sum.
"""
def add_integer(a, b):
    """This function will retrun the sum of a and b."""

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if type(a) is float:
        a = int(a)
    return a + b
