#!/usr/bin/python3
"""
This module contains the isWinner function
which gets a winner in a game
"""


def isWinner(x, nums):
    """
    Function return a winner for the prime game
    """
    def sieve(n):
        """
        Method generates prime numbers up to n
        using sieve of Eratosthenes
        """
        prime = [True for _ in range(n + 1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, n) if prime[p]]

    def simulateGame(n):
        """
        Simulate a single game round
        """
        primes = sieve(n)
        return 'Maria' if len(primes) % 2 != 0 else 'Ben'

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = simulateGame(n)
        wins[winner] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
