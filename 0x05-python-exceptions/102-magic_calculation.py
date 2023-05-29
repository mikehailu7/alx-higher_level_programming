#!/usr/bin/python3
# Author: mikiashailu.
# Projct: ByteCode.
def magic_calculation(a, b):
    res = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            res = res + a ** b / m
        except:
            res = b + a
            break
    return res
