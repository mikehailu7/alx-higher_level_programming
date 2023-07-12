#!/usr/bin/python3
# Author: MikiasHailu
# Project: Triangle
""" This function is called pascal triangle function """


def pascal_triangle(z):
    """ This fucntion will return lists that represent the pascal triangle """
    if z <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != z:
        tri = triangles[-1]
        tmp = [1]
        for m in range(len(tri) - 1):
            tmp.append(tri[m] + tri[m + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
