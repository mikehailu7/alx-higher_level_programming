#!/usr/bin/python3
# MikiasHailu
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    size = my_list[0]
    for z in range(1, len(my_list)):
        if size < my_list[z]:
            size = my_list[z]
        else:
            continue
    return large
