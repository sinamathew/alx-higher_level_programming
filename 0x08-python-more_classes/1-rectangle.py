#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represent a class Rectangle.

    Defines a rectangle by:(based on 0-rectangle.py)

    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle

    Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle

    Raises:
        TypeError: if width or height is not an integer
        ValuError: if width or height is less than 0

    """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): the new width of the rectangle

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): the new width of the rectangle

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
