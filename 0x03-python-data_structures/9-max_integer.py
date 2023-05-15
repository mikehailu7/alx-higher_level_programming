#!/usr/bin/python3
# MikiasHailu
def max_integer(my_list=[]):
# check if the list is empty
    if len(my_list) == 0:
        return
    size = my_list[0]
# check for the list is empty
    for z in range(1, len(my_list)):
        if size < my_list[z]:
            size = my_list[z]
        else:
            continue
    return size
