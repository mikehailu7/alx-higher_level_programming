#!/usr/bin/python3
<<<<<<< HEAD
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
=======
#Author: MikiasHailu
#Fun: IntegersAddition
""" This module is to add integers. """

def add_integer(a, b):
    """ This function will return the addition of two numbers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
>>>>>>> 1f7ed7c8a726f3f75b61141fdf700679989de5ec
    return a + b
