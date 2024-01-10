#!/usr/bin/python3
"""
function to check if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """function to check if all boxes unlock"""
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked_boxes = [0]
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)
