#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    primes = [True] * 10001
    primes[0] = False
    primes[1] = False
    p = 2
    while p**2 <= 10000:
        if primes[p]:
            for i in range(p * p, 10001, p):
                primes[i] = False
        p += 1

    prime_count = [0] * 10001
    for i in range(1, 10001):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:  # If even number of primes, Ben wins
            ben_wins += 1
        else:  # If odd number of primes, Maria wins
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
