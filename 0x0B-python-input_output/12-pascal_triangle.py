#!/usr/bin/python3i
"""
module creates a function hat returns
a list of lists of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to the nth row

    Args:
        n (int): The number of rows in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
