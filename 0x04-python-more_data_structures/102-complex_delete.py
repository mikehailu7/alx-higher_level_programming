#!/usr/bin/python3
# mikiashailu
# complex_delete
def complex_delete(library, value):
    del_key = []
    for key in library:
        if library[key] == value:
            del_key.append(key)
    for key in del_key:
        del library[key]
    return library
