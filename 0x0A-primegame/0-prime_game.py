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
        primes = sieve(n)
        return 'Maria' if len(primes) % 2 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        if not nums:
            break
        n = nums.pop(0)
        winner = simulateGame(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria';
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
