#!/usr/bin/python3
"""Defines a function that writes string to file."""


def write_file(filename="", text=""):
    """Write string to a text file (UTF8).
    Args:
        filename (str): the name of the file to write.
        text (str): strings to write in the file.
    Returns:
        The number of character written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        char_num = file.write(text)
    return char_num
