#!/usr/bin/python3
"""Defines a function that reads file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.
    Args:
        filename (file): the name of file to read.
    """
    with open(filename, 'r', encoding="utf-8") as open_file:
        print(open_file.readlines())
