#!/usr/bin/python3
"""Module that defines write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters written

    Args:
        filename: the name of the file to write to
        text: the text to write to the file

    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
