#!/usr/bin/python3
""" determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """Define a function"""
    dp = [0] + [total+1] * total
    for coin in coins:
        for x in range(coin, total+1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != total+1 else -1
