#!/usr/bin/python3
"""Module that defines a Square class with printing method"""


class Square:
    """A class that defines a square with printing functionality"""

    def __init__(self, size=0):
        """Initialize a new Square with size validation

        Args:
            size (int): the size of the square, defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """Getter for size attribute

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute

        Args:
            value (int): the new size value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # characters"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
