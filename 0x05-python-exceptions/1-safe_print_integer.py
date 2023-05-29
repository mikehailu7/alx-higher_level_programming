#!/usr/bin/python3
# author: MikiasHailu
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except(ValueError, TypeError):
        return False
    else:
        return True
