#!/usr/bin/python3
# Author: MikiasHailu
# project: myinteger
""" This the myint class """


class MyInt(int):
    """ This class is the representaion of my int class """
    def __new__(cls, *args, **kwargs):
        """ This function will create a new obj. """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ This is the eq fuction """
        return int(self) != other

    def __ne__(self, other):
        """ This is the ne function """
        return int(self) == other
