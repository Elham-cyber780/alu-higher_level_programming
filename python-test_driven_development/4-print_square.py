#!/usr/bin/python3
"""Module that defines print_square function for printing a square"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size: the size length of the square (must be an integer)

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
