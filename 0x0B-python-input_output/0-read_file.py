#!/usr/bin/python3
# Author: MikiasHailu
# Project: Readfile
""" This is the read file function """

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
