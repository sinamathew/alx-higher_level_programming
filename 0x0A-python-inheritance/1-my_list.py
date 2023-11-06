#!/usr/bin/python3
"""Module that defines a class MyList."""


class MyList(list):
    """A class that inherit from list."""

    def print_sorted(self):
        """Prints out sorted value of list."""

        return print(sorted(self))
