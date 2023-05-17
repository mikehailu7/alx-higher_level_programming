#!/usr/bin/python3
# mikiasHailu
# Waverage
def weight_average(my_list=[]):
    if my_list and len(my_list):
        dem = 0
        num = 0
        for tup in my_list:
            dem += tup[1]
            num += (tup[0] * tup[1])
        return (num / dem)
    return 0
