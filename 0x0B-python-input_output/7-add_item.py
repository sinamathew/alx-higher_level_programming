#!/usr/bin/python3
"""A scripts that adds all arguments."""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """Add al argument to a Python list.
    Save the item to a file.
    Args:
        Arguments taken in CLI mode.
    """
    try:
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        current_list = []

    current_list.extend(sys.argv[1:])
    save_to_json_file(current_list, "add_item.json")


if __name__ == "__main__":
    add_item()
