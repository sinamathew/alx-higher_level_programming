#!/usr/bin/python3
"""Contains a class to raise exception."""


class BaseGeometry:
    """Just another class that raise exception and many more."""
    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise value and type errors on conditions.

        Args:
            name (str): the name of the parameter.
            value (str): the value of the parameter.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
