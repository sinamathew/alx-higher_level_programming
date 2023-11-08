#!/usr/bin/python3
"""Defines a function that write object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file.
    Args:
        my_obj (obj): the object to be written
        filename (str): the name of the file.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
