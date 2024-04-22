#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Define a function"""
    result = list(zip(*matrix[::-1]))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = result[i][j]
