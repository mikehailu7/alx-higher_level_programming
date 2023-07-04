#!/usr/bin/python3
# Author: MikiasHailu
# fun: Text_indentation.py
"""
This module will indent the text.
"""
def text_indentation(text):
    """This will indent my text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for m in text:
        if flag == 0:
            if m == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if m == '?' or m == '.' or m == ':':
                print(a)
                print()
                flag = 0
            else:
                print(m, end="")
