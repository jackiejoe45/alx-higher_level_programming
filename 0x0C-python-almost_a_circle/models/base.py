#!/usr/bin/python3
"""
This module represents the base class for all other classes in this project
"""
import json


class Base:
    """
    Base class for all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dicts = cls.from_json_string(f.read())
            list_inst = []
            for dict in list_dicts:
                list_inst.append(cls.create(**dict))
            return list_inst
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using the turtle module"""
        import turtle
        import random

        turtle.bgcolor("black")
        turtle.pensize(3)
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()

        for rect in list_rectangles:
            turtle.color((random.random(), random.random(), random.random()))
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.penup()

        for square in list_squares:
            turtle.color((random.random(), random.random(), random.random()))
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.forward(square.width)
            turtle.left(90)
            turtle.forward(square.height)
            turtle.left(90)
            turtle.forward(square.width)
            turtle.left(90)
            turtle.forward(square.height)
            turtle.left(90)
            turtle.penup()

        turtle.exitonclick()
