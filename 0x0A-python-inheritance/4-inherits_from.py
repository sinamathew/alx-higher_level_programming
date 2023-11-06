#!/usr/bin/python3
"""Contain function that check for subclass."""


def is_kind_of_class(obj, a_class):
    """Check if object is a subclass.

    Args:
        obj (any): the object
        a_class (type): a specified class
    Return:
        True if object is a subclass, else False
    """
    return issubclass(type(obj), a_class):
