#!/usr/bin/python3
# mikiashailu
# simple_delete
def simple_delete(abysinan_dic, key=""):
    if key in abysinan_dic:
        del abysinan_dic[key]
    return abysinan_dic
