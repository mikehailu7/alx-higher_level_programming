#!/usr/bin/python3
# Author: MikiasHailu
# Project: Readfile
""" This function is to read a file """

def read_file(filename=""):
    """ This function will read a file """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
