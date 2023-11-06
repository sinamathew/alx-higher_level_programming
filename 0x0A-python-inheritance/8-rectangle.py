#!/usr/bin/python3
"""Contain a class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation of width and height.
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
