#!/usr/bin/python3
# MikiasHailu
def max_integer(my_list=[]):
    if len(my_list) == 0:
# check if the len is empth or not
        return
    size = my_list[0]
# check size of z if it in range
    for z in range(1, len(my_list)):
        if size < my_list[z]:
            size = my_list[z]
        else:
            continue
    return size
