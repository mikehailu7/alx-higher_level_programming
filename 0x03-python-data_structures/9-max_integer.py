#!/usr/bin/python3
# MikiasHailu
def max_integer(my_list=[]):
# check if the list is empty
    if len(my_list) == 0:
        return
    length = my_list[0]
# check for the list is empty
    for z in range(1, len(my_list)):
        if length < my_list[z]:
            length = my_list[z]
        else:
            continue
    return length
