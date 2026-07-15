#!/usr/bin/python3
"""Module that defines a Square class with size"""


class Square:
    """A class that defines a square with a private size attribute"""

    def __init__(self, size):
        """Initialize a new Square with size

        Args:
            size: the size of the square
        """
        self.__size = size
