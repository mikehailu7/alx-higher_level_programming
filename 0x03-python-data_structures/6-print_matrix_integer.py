#!/usr/bin/python3
# MikiasHailu
def print_matrix_integer(matrix=[[]]):
    for z in matrix:
        print(" ".join("{:d}".format(m) for m in z))
