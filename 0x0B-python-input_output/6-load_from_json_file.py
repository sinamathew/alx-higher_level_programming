#!/usr/bin/python3
"""Defines a function to creates an Object."""
import json


def load_from_json_file(filename):
    """Create an object from JSON file.
    Args:
        filename (str): the name of the json file.
    """
    with open(filename) as file:
        return json.load(file)
