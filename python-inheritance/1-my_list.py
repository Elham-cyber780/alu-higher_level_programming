#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """A class that inherits from list with print_sorted method"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
