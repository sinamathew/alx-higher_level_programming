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
            id (int): the identity of the new rectangle.
        Raises:
            TypeError: If either width, height, x or y is not int
            ValueError: If either width or height <= 0
            ValueError: If either x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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


    @width.setter
    def width(self, value):
        """Setter for width.
        Args:
            value (int): the value of width.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height.
        Args:
            value (int): the value of height.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x.
        Args:
            value (int): the value of x.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y.
        Args:
            value (int): the value of y.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area of a new rectangle.
        Returns: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle instance with character #."""
        for i in range(self.__height):
            for i in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """Overides the original string method.
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, \
                self.x, self.y, self.width, self.height)
