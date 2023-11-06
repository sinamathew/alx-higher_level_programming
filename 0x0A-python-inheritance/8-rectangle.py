#!/usr/bin/python3
"""Contain a class that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry.
    Args:
        width (int): the breadth of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width, height):
        """Instantiation of width and height."""
        BaseGeometry.__init__(self)
        if integer_validator("width", width):
            self.__width = width
        if integer_validator("height", height):
            self.__height = height

