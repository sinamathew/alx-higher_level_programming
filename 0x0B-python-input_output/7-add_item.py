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
    arg_list = sys.argv[1:]
    filename = "add_item.json"

    if not path.exists(filename):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write("[]")

    current_list = load_from_json_file(filename)

    current_list.extend(arg_list)

    save_to_json_file(current_list, filename)

if __name__ == "__main__":
    add_item()
