#!/usr/bin/python3
"""Lookup an object attributes and methods."""


def lookup(obj):
    """Function returns list of available attributes and method.

    Args:
        obj: The object to be looked up.

    Return:
        A list of object attributes and method.

        """
    obj_list = dir(obj)
    return obj_list
