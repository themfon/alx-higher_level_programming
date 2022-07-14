#!/usr/bin/python3
"""Base Module"""
import json
import csv
import turtle


class Base:
    """Defines the representation of a Base Object"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base Object
        if id is none, assigns class id incremented by 1
        :param id: identifier of an instantiated base object
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        :param list_dictionaries (list): A list of dictionaries.
        :return:
            If list_dictionaries is None or empty - an empty list
            Otherwise - String representation of list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        :param list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as json_file:
            if list_objs is None or list_objs == []:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        :param json_string (str): A JSON str representation of a list of dicts.
        :return:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        :param dictionary(dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(10, 5)
            else:
                instance = cls(10)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        return:
            If the file does not exist - an empty list.
            Otherwise - a lsit of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dict = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        :param list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        if filename == "Rectangle.csv":
            header = ["id", "width", "height", "x", "y"]
        else:
            header = ["id", "size", "x", "y"]

        with open(filename, "w", newline="") as csv_file:
            if list_objs == [] or list_objs is None:
                csv_file.write("[]")
            else:
                writer = csv.DictWriter(csv_file, fieldnames=header)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        return:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                list_objs = csv.DictReader(csv_file, fieldnames=header)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_objs]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.
        :param list_rectangles (list): A list of Rectangle objects to draw.
        :param list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b1eb34")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#080a04")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#08a04")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.width)
                turt.left(90)
            turt.hideturtle()

        turt.exitonclick()
