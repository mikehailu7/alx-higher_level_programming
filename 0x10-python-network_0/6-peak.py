#!/usr/bin/python3
# Author: MIkiasHailu
""" This is the Algorithm for a list of integers. """
def find_peak(list_of_integers):
    """ This will find a peak in a list of unsorted integers """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
