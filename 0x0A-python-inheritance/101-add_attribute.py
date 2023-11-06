#!/usr/bin/python3
"""Defines the function `add_attribute`."""


def add_attribute(obj, attr_name, attr_value):
    """Function adds a new attribute to an object if possible.
    Args:
        obj (any): the object
        attr_name (str): attribute name
        attr_value (any): attribute value
    Raises:
        TypeError: if the object can't have new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
