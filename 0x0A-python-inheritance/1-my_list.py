#!/usr/bin/python3
"""Module that defines a class MyList."""


class MyList(list):
    """A class that inherit from list.

    Args:
        list (int): the inherited list

    Returns:
        the list
        sorted list

    """
    def print_sorted(self):
        return print(sorted(self))
