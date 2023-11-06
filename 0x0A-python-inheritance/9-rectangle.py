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

    def area(self):
        """Calculate the area of the rectangle.
        Returns:
            The area of rectangle in integer
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
