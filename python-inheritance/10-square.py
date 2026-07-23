#!/usr/bin/python3
"""Module that defines Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square with size

        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
