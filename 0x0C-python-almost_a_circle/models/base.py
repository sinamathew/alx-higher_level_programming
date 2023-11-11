#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """The base of all other classes in this project."""

    def __init__(self, id=NOne):
        """Initialize the class Base."""
        self.__nb_objects = 0

        if id not None:
            self.id = id
        else:
            self.__nb_objects =+ 1
            self.id = self.__nb_objects
