#!/usr/bin/python3
# author: MikiasHailu.
# safe list printing.
def safe_print_list(my_list=[], x=0):
    z = 0
    for k in range(x):
        try:
            print(my_list[k], end="")
            z = z + 1
        except IndexError:
            break
    print()
    return z
