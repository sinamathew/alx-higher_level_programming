#!/usr/bin/python3
"""Contain function that kind of an object."""


def is_kid_of_class(obj, a_class):
    """Check if object is kind of specified class.

    Args:
        obj (obj): the object
        a_class (instances): a specified class

    Return:
        True if object is a kind of the specified class, else False

    """
    return isinstance(obj, a_class)
