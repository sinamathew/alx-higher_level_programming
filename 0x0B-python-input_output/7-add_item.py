#!/usr/bin/python3
"""A scripts that adds all arguments."""
import sys
import json
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """Add al argument to a Python list.
    Save the item to a file.
    Args:
        Arguments taken in CLI mode.
    """
    filename = "add_item.json"
    try:
        current_list = load_from_json_file(filename)
    except FileNotFoundError:
        current_list = []

    arg_list = sys.argv[1:]
    current_list.extend(arg_list)
    save_to_json_file(current_list, filename)


if __name__ == "__main__":
    add_item()
