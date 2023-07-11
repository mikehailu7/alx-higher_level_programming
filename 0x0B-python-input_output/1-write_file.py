#!/usr/bin/python3
# Author: MikiasHailu
# Project: writefile
""" This function is a writefile function """


def write_file(filename="", text=""):
    """ This function wll write into filename and text """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
