#!/usr/bin/python3
"""Defines a class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []
        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

