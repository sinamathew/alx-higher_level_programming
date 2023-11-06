#!/usr/bin/python3
"""Modules contain function that check instance of an object."""


def is_same_class(obj, a_class):
    """Check if object instance is of specified class.

    Args:
        obj (obj): the object
        a_class (instances): a specified class

    Return:
        True if object is an instance of the specified class, else False

    """
    return type(obj) == a_class
