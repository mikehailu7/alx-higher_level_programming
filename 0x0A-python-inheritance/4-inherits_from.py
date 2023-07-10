#!/usr/bin/python3
#Author: MikiasHailu
#project: only sub class of
""" This function is called the inherits from """

def inherits_from(obj, a_class):
    """ This function will returns true if obj is a subclass of a class """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
