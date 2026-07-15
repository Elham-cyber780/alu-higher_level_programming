#!/usr/bin/python3
"""Module that defines a Rectangle class with area and perimeter"""


class Rectangle:
    """A class that defines a rectangle with area and perimeter methods"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): the width of the rectangle, defaults to 0
            height (int): the height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Args:
            value (int): the new width value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute

        Args:
            value (int): the new height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter

        Returns:
            int: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
