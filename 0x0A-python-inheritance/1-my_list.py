#!/usr/bin/python3
# Author: MikiasHailu
# project: Mylist
""" This is the mylist class """


class MyList(list):
    """ this is the mylist class with a list as a parameter """
    def __init__(self):
        """ This function is for initalizaiton """
        super().__init__()

    def print_sorted(self):
        """ This function will print the list which is sorted """
        print(sorted(self))
