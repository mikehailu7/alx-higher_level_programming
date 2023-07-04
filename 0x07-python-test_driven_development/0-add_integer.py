#!/usr/bin/python3
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
    return a + b
