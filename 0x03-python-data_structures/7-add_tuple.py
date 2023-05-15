#!/usr/bin/python3
# MikiasHailu
def add_tuple(tuple_a=(), tuple_b=()):
    sizeB = len(tuple_b)
    sizeA = len(tuple_a)
    if sizeA < 1:
        tuple_a = (0, 0)
    elif sizeA < 2:
        tuple_a = (tuple_a[0], 0)
    if sizeB < 1:
        tuple_b = (0, 0)
    elif sizeB < 2:
        tuple_b = (tuple_b[0], 0)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
