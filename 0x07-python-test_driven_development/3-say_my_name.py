#!/usr/bin/python3
# Author: MikiasHailu
# fun: Say my name
"""
This module is called say my name.
This module will print the firstname and lastname.
"""
def say_my_name(first_name, last_name=""):
    """This function will Print the first and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
