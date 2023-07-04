#!/usr/bin/python3
# Author: mikiashailu
# Fun: lazy_matrix_mul
""" This function will multiply the matrix """
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices using np.

    Argument:
        m_b: The second matrix.
        m_a: The first matrix.
    Return:
        will return the product.
    """
    return (np.matmul(m_a, m_b))
