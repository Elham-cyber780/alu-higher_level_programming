#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """A class that defines base geometry with area method"""

    def area(self):
        """Raises an Exception with message area() is not implemented"""
        raise Exception("area() is not implemented")
