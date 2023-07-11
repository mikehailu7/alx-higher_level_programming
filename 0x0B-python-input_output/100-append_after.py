#!/usr/bin/python3
# Author: MikiasHailu
# Project: Search
""" This fucntion is called append_after  """

def append_after(filename="", search_string="", new_string=""):
    """ This fucntion will append the filename the search string and new string """
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
