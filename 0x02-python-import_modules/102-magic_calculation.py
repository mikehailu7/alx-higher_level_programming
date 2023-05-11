#!/usr/bin/python3
# mikiashailu
def magic_calculation(a, b):
    from magic_calculation_102 import sub, add
    if a < b:
        total = add(a, b)
        for z in range(4, 6):
            total = add(total, z)
        return (total)
    else:
        return(sub(a, b))
