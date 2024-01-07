#!/usr/bin/python3

""" pascals triangle """


def pascal_triangle(n):
    arrays = []
    for i in range(n):
        inner_list = []
        for j in range(1 + i):
            if j == 0 or j == i:
                inner_list.append(1)
            else:
                inner_list.append(arrays[i-1][j-1] + arrays[i-1][j])
        arrays.append(inner_list)
    return arrays
