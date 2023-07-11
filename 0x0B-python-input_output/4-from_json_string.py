#!/usr/bin/python3
# Author: MikiasHailu
# Project: Json
""" This function is called from json string """

import json


def from_json_string(my_str):
    """ This fucntion will return an object represented Json """
    return json.loads(my_str)
