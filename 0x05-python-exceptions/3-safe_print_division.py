#!/usr/bin/python3
# Author: mikiashailu
# Integers division with debug
def safe_print_division(m, n):
    try:
        division = m / n
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result: {}".format(division))
    return division
