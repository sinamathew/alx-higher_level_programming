#!/usr/bin/python3
"""Defines a function that reads file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.
    Args:
        filename (str): the name of file to read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
