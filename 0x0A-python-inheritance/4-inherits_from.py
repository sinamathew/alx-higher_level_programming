#!/usr/bin/python3
"""Contain function that check for subclass."""


def inherits_from(obj, a_class):
    """Check if object is a subclass.

    Args:
        obj (any): the object
        a_class (type): a specified class
    Return:
        True if object is a subclass, else False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
