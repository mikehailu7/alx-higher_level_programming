#!/usr/bin/python3
# mikiasHailu
import sys
count = len(sys.argv) - 1
if count == 1:
    print("1 argument.")
elif count == 0:
    print("0 argument:")
else:
    print("{} arguments:":".format(count))
for z in range(count):
     print("{}: {}".format(z + 1, sys.argv[z + 1]))
