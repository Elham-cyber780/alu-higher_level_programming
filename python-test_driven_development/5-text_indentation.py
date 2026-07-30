#!/usr/bin/python3
"""Module that defines text_indentation function"""


def text_indentation(text):
    """Prints text with 2 new lines after each . ? and : character

    Args:
        text: the text to print (must be a string)

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
