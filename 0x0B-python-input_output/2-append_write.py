#!/usr/bin/python3
# Author: MIkiasHailu
# Project: Appendfile
""" This function will appendwrite """


def append_write(filename="", text=""):
    """ This fucntion will append the fileame and text """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
