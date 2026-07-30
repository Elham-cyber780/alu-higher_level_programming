#!/usr/bin/python3
"""Module that defines add_integer function for adding two integers"""


def add_integer(a, b=98):
    """Adds two integers or floats and returns an integer

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
