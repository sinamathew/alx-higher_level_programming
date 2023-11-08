#!/usr/bin/python3
"""Define function that return an object."""
import json


def from_json_string(my_str):
    """Just to return, nothing more.
    Args:
        my_str (str): python data structure.
    Returns:
        the object represented by JSON.
    """
    return json.loads(my_str)
