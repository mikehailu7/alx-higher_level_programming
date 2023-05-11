#!/usr/bin/python3
# mikiashailu
from sys import argv
if __name__ == "__main__":
add = 0
for z in argv[1:]:
    add += int(z)
print("{:d}".format(add))
