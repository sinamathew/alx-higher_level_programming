#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represent a class Rectangle.

    Defines a rectangle by:(based on 3-rectangle.py)

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

    def area(self):
        """Gets the area of the rectangle.

        Returns:
            the product of width and height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Gets the perimeter of the rectangle.

        Returns:
            the sum of width and height multipied by 2

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Get the size of string as shape.

        Returns:
            Nothing: if height or width is 0
            rect_str (#): representing the height and width

        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """String representation.

        Returns:
            Official string representation

        """
        return f"Rectangle({self.__width}, {self.__height})"
