#!/usr/bin/python3
"""Defines a class Base"""
import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """Another static method.
        Args:
            json_string (json): a string representing a list of dictionaries
        Returns:
            empty list if file is none else, the JSON string representation
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create something new.
        Args:
            dictionary (kwargs): contains a dictionary.
        Returns:
            an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances of the current class.
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                for dictionary in json_list:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances to be serialized.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for instance in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([instance.id, instance.width,
                                     instance.height, instance.x, instance.y])
                elif cls.__name__ == "Square":
                    writer.writerow([instance.id,
                                     instance.size, instance.x, instance.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]),
                                       int(row[2]), int(row[3]), int(row[0]))
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Create a turtle screen"""
        screen = turtle.Screen()

        t = turtle.Turtle()

        t.speed(1)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        screen.exitonclick()


if __name__ == "__main__":
    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10),
                       Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
