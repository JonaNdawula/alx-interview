#!/usr/bin/python3
"""
This module contains a function
that rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
