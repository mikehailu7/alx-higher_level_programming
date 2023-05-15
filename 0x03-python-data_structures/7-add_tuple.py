#!/usr/bin/python3
# MikiasHailu
add_tuple = __import__('7-add_tuple').add_tuple
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    if lenA < 1:
        tuple_a = (0, 0)
    elif lenA < 2:
        tuple_a = (tuple_a[0], 0)
    if lenB < 1:
        tuple_b = (0, 0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
