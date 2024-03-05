#!/usr/bin/python3
"""
The Island perimter problem
"""


def island_perimeter(grid):
    """Island perimeter problem"""
    perimter = 0
    len1 = len(grid)
    len2 = len(grid[1])
    for id1, v1 in enumerate(grid):
        count = 0
        for id2, v2 in enumerate(v1):
            if v2 == 1:
                if (id2 - 1) < 0 or grid[id1][id2 - 1] == 0:
                    count += 1
                if (id2 + 1) == len2 or grid[id1][id2 + 1] == 0:
                    count += 1
                if (id1 - 1) < 0 or grid[id1 - 1][id2] == 0:
                    count += 1
                if (id1 + 1) == len1 or grid[id1 + 1][id2] == 0:
                    count += 1
        perimter += count
    return (perimter)
