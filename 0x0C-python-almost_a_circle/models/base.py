#!/usr/bin/python3

import turtle
import json
import csv  # Import the csv module


class Base:
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            dummy_instance = None

        if dummy_instance is not None:
            dummy_instance.update(**dictionary)  # Update attributes
            return dummy_instance
        else:
            return None

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"  # Generate the filename
        try:
            with open(filename, "r") as file:
                data = file.read()  # Read the JSON data from the file
                if data:
                    data_list = cls.from_json_string(data)
                    instances_list = [cls.create(**d) for d in data_list]
                    return instances_list
                else:
                    return []
        except FileNotFoundError:
            return []  # File doesn't exist, return an empty list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV and save to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                        ])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from CSV file and returns a list of objects.
        """
        filename = cls.__name__ + ".csv"
        obj_list = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        # Create a dummy instance with non-zero values
                        obj = cls(1, 1, 1, 1, id)
                        obj.update(id, width, height, x, y)
                        obj_list.append(obj)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        # Create a dummy instance with non-zero values
                        obj = cls(1, 1, 1, id)
                        obj.update(id, size, x, y)  # Update with actual values
                        obj_list.append(obj)
        except FileNotFoundError:
            pass

        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.title("Shapes Drawing")

        t = turtle.Turtle()
        t.speed(1)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.penup()

        window.exitonclick()
