#!/usr/bin/python3
# MikiasHailu
# check whether it is divisible by 2
def divisible_by_2(my_list=[]):
    Nlist = my_list.copy()
    for m in range(0, len(my_list)):
        if my_list[m] % 2 == 0:
            Nlist[m] = 1
        else:
            Nlist[m] = 0
    return Nlist
