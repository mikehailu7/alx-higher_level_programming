#!/usr/bin/python3
# mikiashailu
if __name__ == "__main__":
    from calculator_1 import mul, add, div, sub
    b = 5
    a = 10
    print("{} + {} = {}".format(b, a, add(b, a)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(b, a, mul(b, a)))
    print("{} / {} = {}".format(a, b, div(a, b)))
