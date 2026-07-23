#!/usr/bin/python3
"""Module that defines class_to_json function"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of an object

    Args:
        obj: an instance of a Class

    Returns:
        dictionary description of the object
    """
    return obj.__dict__
