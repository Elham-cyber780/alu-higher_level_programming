#!/usr/bin/python3
"""Module that defines a Square class with position"""


class Square:
    """A class that defines a square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with size and position

        Args:
            size (int): the size of the square, defaults to 0
            position (tuple): the position of the square, defaults to (0, 0)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position attribute

        Returns:
            tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute

        Args:
            value (tuple): the new position value

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # characters at the given position"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
