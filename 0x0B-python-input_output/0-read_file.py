#!/usr/bin/python3
# Author: MikiasHailu
# Project: Readfile
""" This is the read file function """


def read_file(filename=""):
    """" This is thre readfile function which prints filename """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
