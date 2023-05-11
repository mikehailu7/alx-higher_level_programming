#!/usr/bin/python3
# mikias hailu
import sys    
if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 1:
        print("1 arguments.")
    elif count == 0:
        print("0 argument:")
    else:
        print("{} arguments:".format(count))
    for k in range(count):
        print("{}: {}".format(k + 1, sys.argv[k + 1]))
