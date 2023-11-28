#!/usr/bin/python3

"""
Pascal triangle function
"""


def pascal_triangle(n):
    """"
    Evaluate the pascal triangle
    args:
        n: integer
    return:
        a list of lists of integer
    """

    pas = []

    if n <= 0:
        return pas
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                row.append(1)
            else:
                row.append(pas[i - 1][j - 1] + pas[i - 1][j])
        pas.append(row)
    return pas
