#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """The base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
