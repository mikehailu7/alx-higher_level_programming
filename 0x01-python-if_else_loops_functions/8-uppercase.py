#!/usr/bin/python3
def uppercase(str):
    for Uc in str:
        if ord(Uc) >= 97 and ord(Uc) <= 122:
            Uc = chr(ord(Uc) - 32)
        print("{:s}".format(Uc), end='')
    print('\n', end="")
