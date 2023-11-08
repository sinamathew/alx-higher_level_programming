#!/usr/bin/python3
"""Defines a function that append string to file."""


def append_write(filename="", text=""):
    """Append string to the end of a file.
    Args:
        filename (str): the name of file to append.
        text (str): string to appent to the file (UTF8).
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
