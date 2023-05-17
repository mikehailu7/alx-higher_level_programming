#!/usr/bin/python3
# mikiasHailu
# matrix
def square_matrix_simple(matrix=[]):
    return [list(map((lambda c: c * c), elm)) for mu in matrix]
