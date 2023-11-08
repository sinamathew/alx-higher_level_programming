#!/usr/bin/python3
"""Defines a function that returns JSON representation."""
import json


def to_json_string(my_obj):
    """Just to return, nothing more.
    Args:
        my_obj (obj): an object (string).
    Returns:
        The JSON representation of an object.
    """
    return json.dumps(my_obj)
