#!/usr/bin/python3
# Author: mikiashailu
# Print and count integers
def safe_print_list_integers(list_1=[], x=0):
    m = 0
    for n in range(x):
        try:
            print("{:d}".format(list_1[n]), end="")
            m = m + 1
        except(ValueError, TypeError):
            continue
    print()
    return m
