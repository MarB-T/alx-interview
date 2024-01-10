#!/usr/bin/python3

"""
Find if all th 'boxes' can be unlocked
"""


def canUnlockAll(boxes):
    """function to check if all boxes unlock"""
    all_index = set(list(range(len(boxes))))
    keys = {0}
    keys.update(boxes[0])
    for _ in range(3):
        for i in range(len(boxes)):
            if i in keys:
                keys.update(boxes[i]) 
    return (keys == all_index)
