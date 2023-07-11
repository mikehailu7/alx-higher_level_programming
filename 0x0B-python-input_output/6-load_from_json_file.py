#!/usr/bin/python3
# Author: MikiasHailu
# Project: Load
""" This function is called load from json file """

import json


def load_from_json_file(filename):
    """ This function will load an object to json """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
