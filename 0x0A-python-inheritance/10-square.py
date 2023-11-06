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
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self, size, size)

    def area(self):
        """Defines the area of the square.
        Returns:
            the value of the area.
        """
        return self.__size * self.__size
