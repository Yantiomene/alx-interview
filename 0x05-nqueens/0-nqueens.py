#!/usr/bin/python3

"""Defines function to solve the n queens problem
"""


def queens(n, i, a, b, c):
    """Solved the n queens problem recursively
       Args:
           n: size of the chess
           i: index to interate
           a: list of correct queens position
           b: list of queens positions
           c: list of queens positions
       Return:
            The list of correct queens position
    """

    if i < n:
        for j in range(n):
            if j not in a and j + i not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def print_solution(n):
    """Prints solutions for n queens problems
       Args:
           n: chess size
       Returns:
              None
    """
    for sol in queens(n, 0, [], [], []):
        solution = [[i, sol[i]] for i in range(n)]
        print(solution)


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solution(N)
