#!/usr/bin/python3
"""Defines a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class Rectangle.
        Args:
            width (int): the rectangle width.
            height (int): the rectangle height.
            y (int): maybe the position
            x (int): maybe the position
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width.
        Returns: The width.
        """
        return self.__width

    @property
    def height(self):
        """Getter for height.
        Returns: The height.
        """
        return self.__height

    @property
    def x(self):
        """Getter for x.
        Returns: The x.
        """
        return self.__x

    @property
    def y(self):
        """Getter for y.
        Returns: The y.
        """
        return self.__y

    @property
    def width(self):
        """Getter for width.
        Returns: The width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.
        Args:
            value (int): the value of width.
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height.
        Args:
            value (int): the value of height.
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x.
        Args:
            value (int): the value of x.
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y.
        Args:
            value (int): the value of y.
        """
        self.__y = value
