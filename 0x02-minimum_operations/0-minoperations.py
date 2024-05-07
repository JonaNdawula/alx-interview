#!/usr/bin/env python3


"""
Contains the function minOperations
that calculates the fewest number of
operations needed to result in exactly n H
chararacters in the file
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file

    Parameters:
    n : The target number of H characters

    Returns:
    minimum number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
