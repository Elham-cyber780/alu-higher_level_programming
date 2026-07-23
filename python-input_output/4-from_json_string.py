#!/usr/bin/python3
"""Module that defines from_json_string function"""
import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string

    Args:
        my_str: the JSON string to convert to a Python object

    Returns:
        the Python object represented by the JSON string
    """
    return json.loads(my_str)
