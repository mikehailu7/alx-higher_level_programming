#!/usr/bin/python3
# mikiasHailu
# sorted_dictionary
def print_sorted_dictionary(abysnian_dic):
    for key in sorted(abysnian_dic.keys()):
        print("{:s}: {}".format(key, abysnian_dic[key]))
