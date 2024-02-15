#!/usr/bin/python3
""" Prime game
"""


def isWinner(x, nums):
    """ Function to determine the winner
    """

    def generatePrimes(n):
        """Returns the list of primes numbers lest than n
        """
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        return [p for p in range(2, n + 1) if prime[p]]

    nWinBen = 0
    nWinMar = 0

    gen_primes = generatePrimes(max(nums))
    for i in range(x):
        primes = [p for p in gen_primes if p <= nums[i]]
        if len(primes) % 2 == 0:
            nWinBen += 1
        else:
            nWinMar += 1
    if nWinBen == nWinMar:
        return None
    elif nWinBen > nWinMar:
        return 'Ben'
    else:
        return 'Maria'
