#!/usr/bin/python3
"""Module that defines Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle with width and height

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
