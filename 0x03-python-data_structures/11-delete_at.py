#!/usr/bin/python3
# MikiasHailu
# delete_at: This function will delete at a specified position.
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
