#!/usr/bin/python3
# Author: MikiasHailu
# Project: Readfile
""" This function is to read a file """

def read_file(filename=""):
    """ This function will Reads a text file. """
    with open(filename, 'r') as f:
        print(f.read(), end='')
