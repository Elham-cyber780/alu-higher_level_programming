#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """A class that defines base geometry with validation"""

    def area(self):
        """Raises an Exception with message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is a positive integer

        Args:
            name: the name of the parameter
            value: the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
