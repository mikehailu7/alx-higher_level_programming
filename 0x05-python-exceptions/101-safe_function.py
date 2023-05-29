#!/usr/bin/python3
# Author: mikiashailu
# Safe function
def safe_function(fun, *args):
    try:
        m = fun(*args)
        return m
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
