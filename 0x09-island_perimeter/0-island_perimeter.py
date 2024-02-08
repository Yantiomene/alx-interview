#!/usr/bin/python3

"""Module that defines the function get the perimeter of an island
"""


def island_perimeter(grid):
    """
    Return the Perimeter of an island in the grid
    """

    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])

    perim = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if j == 0 or grid[i][j - 1] == 0:
                    perim += 1
                if i == 0 or grid[i - 1][j] == 0:
                    perim += 1
                if j == col - 1 or grid[i][j + 1] == 0:
                    perim += 1
                if i == row - 1 or grid[i + 1][j] == 0:
                    perim += 1
    return perim
