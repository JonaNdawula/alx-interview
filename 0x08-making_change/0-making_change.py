#!/usr/bin/python3
"""
This module contains
a method that Returns
the fewest number of coins needed to meet
a given total
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet
    a given total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if total >= coin:
            count += total // coin
            total %= coin

    if total != 0:
        return -1

    return count
