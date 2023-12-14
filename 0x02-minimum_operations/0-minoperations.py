#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations
    Args:
         n: int
    Return:
           an integer
    """
    if n == 1:
        return 0

    divisor = 2
    operations = 0

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor

        divisor += 1

    return operations
