#!/usr/bin/python3
"""Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix
    """
    M = [[row[i] for i in range(0, len(row))] for row in matrix]

    n = len(M)

    for i in range(0, n):
        for j in range(0, n):
            matrix[j][n - 1 - i] = M[i][j]
