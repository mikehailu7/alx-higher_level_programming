#!/usr/bin/python3
# MikiasHailu
# This function will delete 
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
# This will delete in the specified location
    del my_list[idx]
    return my_list
