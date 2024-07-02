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
        if n < 2:
            return []
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        primes = []
        for p in range(2, n + 1):
            if prime[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    prime[i] = False
        return primes

    def simulateGame(n):
        """
        Simulate a single game round
        """
        if n == 1:
            return 'Ben'
        primes = sieve(n)
        return 'Maria' if len(primes) % 2 == 1 else 'Ben'

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
