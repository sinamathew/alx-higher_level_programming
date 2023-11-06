#!/usr/bin/python3
"""Defines a class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """InheritRectangle from (9-rectangle.py)."""
    def __init__(self, size):
        """Instantiation with size.
        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(self, size, size)
        self.__size = size

    def area(self):
        """Defines the area of the square.
        Returns:
            the value of the area.
        """
        return self.__size * self.__size

    def __str__(self):
        """Description of the class Square.
        Returns:
            the square description.
        """
        return "[Square] {}/{}".format(self.__width, self.__height)
