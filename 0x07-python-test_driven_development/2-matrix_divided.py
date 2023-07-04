#!/usr/bin/python3
# author: mikiashailu
# fun: Divide a matrix
""" This module will divid a matrix """
def matrix_divided(matrix, div):
    """This will divide a matrix by an integer"""
    import decimal
    EroMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(EroMessage)
    length_row = []
    row_cnt = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(EroMessage)
        length_row.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(EroMessage)
        row_cnt = row_cnt + 1
    if len(set(length_row)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_mtrx = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_mtrx
