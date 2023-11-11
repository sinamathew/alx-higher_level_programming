#!/usr/bin/python3
"""Defines the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
    """Initializes Square.
    Args:
        size: (int): the size of a new square
        x (int): x axis position of a new square
        y (int): y axis position of a new square
        id (int): identity of a new square
    """
    super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints the...I don't know.
        Returns: the string.....whatever.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, \
                self.size)
