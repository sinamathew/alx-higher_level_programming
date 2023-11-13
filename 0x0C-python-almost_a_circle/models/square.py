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

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates square and assign attributes."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def __str__(self):
        """Prints the...I don't know.
        Returns: the string.....whatever.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """Returns the dictionary representation of Square."""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
