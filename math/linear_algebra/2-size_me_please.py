#!/usr/bin/env python3
"""
This module contains a function that calculates the shape of a matrix.
The shape of a matrix is returned as a list of integers representing its dimensions.
"""

def matrix_shape(matrix):
    """
    Returns the shape of the given matrix.

    A matrix's shape is represented as a list of integers where each integer
    corresponds to the number of elements in each dimension of the matrix.

    Args:
        matrix (list): A 2D or multi-dimensional list representing the matrix.

    Returns:
        list: A list of integers representing the dimensions (shape) of the matrix.

    Example:
        For matrix = [[1, 2], [3, 4]],
        the function will return [2, 2] because the matrix has 2 rows and 2 columns.
    """
    shape = []
    while isinstance(matrix, list):  # Check if the current level is a list
        shape.append(len(matrix))  # Add the length of the current list (number of rows or sublists)
        matrix = matrix[0]  # Move to the first element (a sublist) for the next dimension
    return shape

