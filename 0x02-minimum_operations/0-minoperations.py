#!/usr/bin/python3
""" Minimum Operations
    """

MAXN = 100001

# stores smallest prime factor for every number
spf = [1] * (MAXN + 1)

# Calculating SPF (Smallest Prime Factor) for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    """ Calculate all spf """
    for i in range(2, MAXN + 1):
        if spf[i] == 1:  # If the number is prime
            for j in range(i, MAXN + 1, i):
                if spf[j] == 1:
                    spf[j] = i

def minOperations(n):
    """ Minimum Operations needed to get n H characters """  
    if n <= 1:
        return 0
    
    sieve()
    
    sum_operations = 0
    while n > 1:
        sum_operations += spf[n]
        n = n // spf[n]

    return sum_operations
