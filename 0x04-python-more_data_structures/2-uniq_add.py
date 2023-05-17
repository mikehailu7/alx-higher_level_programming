#!/usr/bin/python3
# mikiashailu
# uniqueAddition
def uniq_add(my_list=[]):
    total = 0
    for z in set(my_list):
        total = total + z
    return total
