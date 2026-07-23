#!/usr/bin/python3
"""Module that defines to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj: the object to convert to JSON

    Returns:
        the JSON string representation of the object
    """
    return json.dumps(my_obj)
