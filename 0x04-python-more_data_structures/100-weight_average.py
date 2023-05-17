#!/usr/bin/python3
# mikiasHailu
# Waverage
def weight_average(my_list=[]):
    if my_list and len(my_list):
        scr = 0
        wei = 0
        for chc in my_list:
            wei = wei + chc[1]
            scr = scr + (chc[0] * chc[1])
        return (num / dem)
    return 0
