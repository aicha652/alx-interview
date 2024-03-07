#!/usr/bin/python3
"""Define pascal_triangle function"""


def pascal_triangle(n):
    """ pascal_triangle function """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]
        for j in range(1, i):
            next_row.append(prev_row[j - 1] + prev_row[j])
        next_row.append(1)
        triangle.append(next_row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
