#!/usr/bin/python3
"""Change comes from within
"""


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to meet total
    """

    if total == 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        quo = total // coin
        count += quo
        total -= quo * coin

    if total != 0:
        return -1

    return count
