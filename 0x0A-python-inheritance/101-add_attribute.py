#!/usr/bin/python3
# Author: MikiasHailu
# Project: CanI

""" This function will add attributes to an objects. """


def add_attribute(obj, att, value):
    """ This function will add a new attribute to an obj. """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
