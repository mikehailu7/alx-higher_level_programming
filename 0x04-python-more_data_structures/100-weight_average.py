#!/usr/bin/python3
# mikiasHailu
# Waverage
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        dem = 0
        for chc in my_list:
            dem = dem + chc[1]
            num = num + (chc[0] * chc[1])
        return (num / dem)
    return 0
