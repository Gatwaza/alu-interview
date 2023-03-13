#!/usr/bin/python3

"""
Pascal's triangle print
"""

def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal triangle of n.
    """

    if n <= 0:
        return []

    triangle = [[1], [1, 1]]

    if n <= 2:
        return triangle[:n]

    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle 
