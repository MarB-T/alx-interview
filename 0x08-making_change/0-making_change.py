#!/usr/bin/python3
"""
Function to determine the fewest number of coins
to find a given total
"""


def makeChange(coins, total):
    """function to find change"""
    if total < 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] >= total:
        return -1
    return dp[total]
