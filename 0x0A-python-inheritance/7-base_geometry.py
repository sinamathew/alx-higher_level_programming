#!/usr/bin/python3
"""Contains a class to raise exception."""


class BaseGeometry:
    """Just another class that raise exception and many more."""
    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise value and type errors on conditions."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
