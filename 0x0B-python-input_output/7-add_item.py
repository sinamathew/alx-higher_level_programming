#!/usr/bin/python3
"""A scripts that adds all arguments."""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item:
    """Add al argument to a Python list.
    Save the item to a file.
    Args:
        Arguments taken in CLI mode.
    """
    arguments = sys.argv
    save_to_json_file(my_list, add_item.json)
