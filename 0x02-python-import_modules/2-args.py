#!/usr/bin/python3
if __name__ == "__main__":
count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))
for z in range(count):
     print("{}: {}".format(z + 1, sys.argv[z + 1]))
