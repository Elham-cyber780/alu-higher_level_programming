#!/usr/bin/python3
"""Module that defines append_write function"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns number of characters added

    Args:
        filename: the name of the file to append to
        text: the text to append to the file

    Returns:
        the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
