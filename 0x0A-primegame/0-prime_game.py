#!/usr/bin/python3
"""Create a function isWinner"""


def isWinner(x, nums):
    """Function to check if a number is prime"""
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    """Function to simulate the game round"""
    def play_round(n):
        primes = [i for i in range(2, n+1) if is_prime(i)]
        turn = 0
        while primes:
            if turn == 0:
                choice = primes.pop(0)
            else:
                choice = primes.pop()
            primes = [p for p in primes if p % choice != 0]
            turn = 1 - turn
        return 'Maria' if turn == 1 else 'Ben'

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
