#!/usr/bin/python3
# Author: MikiasHailu
# project: SaveObj
""" This fucntion is save to jason file """

import json


def save_to_json_file(my_obj, filename):
    """ This function will save an Object to a text file """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
