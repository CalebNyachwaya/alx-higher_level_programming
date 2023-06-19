#!/usr/bin/python3
""" Defining a class named Base """
import json


class Base:
    """ Declaring a private class variable """
    __nb_objects = 0

    """ Defining the constructor of the class """
    def __init__(self, id=None):
        """
        Constructor for the Base class.
        """
        if id is not None:
            """ If id is not None, assign it to the id attribute of
            the object """
            self.id = id
        else:
            """If id is None, increment the private class variable
            by 1 and assign it to the id attribute of the object"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            """If the list of dictionaries is empty or None,
            return the string "[]"""
            return "[]"
        else:
            """Otherwise, return the JSON string representation
            of list_dictionaries"""
            return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            json_str = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file
        with the name "<Class name>.json"
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_str = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_str)
        instances = []
        for dictionary in list_dicts:
            instance = cls.create(**dictionary)
            instances.append(instance)
        return instances
