#!/usr/bin/env python3
"""
Module that provides a function to compute the summation
of squares from 1 to n.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares from 1 to n.

    Args:
        n (int): The upper limit of the summation.

    Returns:
        int: The sum of squares from 1 to n.
        None: If n is not a valid positive integer.
    """
        if not isinstance(n, int) or n < 1:
                return None

        return n * (n + 1) * (2 * n + 1) // 6
