#!/usr/bin/python3
# mikiashailu
if __name__ == "__main__":
    from calculator_1 import mul, add, div, sub
    b = 5
    a = 10
    print("{:d} * {:d} = {:d}".format(b, a, mul(b, a)))
    print("{:d} + {:d} = {:d}".format(b, a, add(b, a)))
    print("{:d} / {:d} = {:d}".format(b, a, div(b, a)))
    print("{:d} - {:d} = {:d}".format(b, a, sub(b, a)))
