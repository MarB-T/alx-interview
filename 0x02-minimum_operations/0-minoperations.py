#!/usr/bin/python3
'''
Minimun  number of Operations
'''


def minOperations(n: int) -> int:
    '''Calculate the minimum number of operations'''
    current = 1
    holder = 0
    count = 0
    while (current < n):
        if holder == 0:
            holder = current
            count += 1
        if current == 1:
            current += holder
            count += 1
            continue
        rem = n - current
        if rem < holder:
            return 0
        if rem % current == 0:
            holder = current
            current += holder
            count += 2
        else:
            current += holder
            count += 1
    if current != n:
        return 0
    return count
