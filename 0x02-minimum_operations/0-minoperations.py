#!/usr/bin/python3
"""define a method that calculates the fewest number of
operations needed to result in exactly n H characters
in the file."""


def minOperations(n):
    """create a minOperations method"""
    operation = 0
    firstPrime = 2

    while(firstPrime <= n):
        if (n % firstPrime == 0):
            operation += firstPrime
            n = n / firstPrime
        else:
            firstPrime += 1
    return (operation)
