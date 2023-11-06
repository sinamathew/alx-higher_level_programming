#!/usr/bin/python3
"""Contains a class to raise exception."""


class BaseGeometry:
    """Just another class that raise exception."""
    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")
