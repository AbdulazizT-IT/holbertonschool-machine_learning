#!/usr/bin/env python3
"""
Module that provides a function to compute
the derivative of a polynomial.
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): List of coefficients where the index
        represents the power of x.

    Returns:
        list: A new list of coefficients representing
        the derivative.
        None: If poly is not valid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for element in poly:
        if not isinstance(element, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    derivative = []

    for power in range(1, len(poly)):
        derivative.append(poly[power] * power)

    return derivative
