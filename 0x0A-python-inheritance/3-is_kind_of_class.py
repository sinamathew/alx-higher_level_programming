#!/usr/bin/python3
"""Contain function that kind of an object."""


def is_kind_of_class(obj, a_class):
    """Check if object is kind of specified class.

    Args:
        obj (any): the object
        a_class (type): a specified class
    Return:
        True if object is a kind of the specified class, else False
    """
    if isinstance(obj, a_class):
        return True
    return False
