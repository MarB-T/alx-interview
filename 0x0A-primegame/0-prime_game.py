#!/usr/bin/python3
"""Determining the prime game for winner"""
import math


def isWinner(x, nums):
    '''The prime game to determine the winner'''

    def is_prime(n):
        """check if a number is prime"""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        val = math.isqrt(n)
        for d in range(3, val + 1, 2):
            if n % d == 0:
                return False
        return True

    def gen_prime(prime_lis):
        """genearet prime from a list"""
        prime = []
        for val in prime_lis:
            if is_prime(val):
                prime.append(val)
        return prime

    playe = ['X', 'Y']
    player = {'X': 0,  'Y': 0}
    for i in range(x):
        number = nums[i]
        num_lis = range(1, number)
        prime = gen_prime(num_lis)
        number = ((len(prime) + 1) % 2)
        player[playe[number]] += 1
    if player['X'] > player['Y']:
        return "Maria"
    return "Ben"
