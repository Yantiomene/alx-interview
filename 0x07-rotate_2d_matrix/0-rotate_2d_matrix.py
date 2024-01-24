#!/usr/bin/python3
"""Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix in place
    """

    n = len(matrix)

    # Transpose the matrix in-place
    for i in range(0, n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
