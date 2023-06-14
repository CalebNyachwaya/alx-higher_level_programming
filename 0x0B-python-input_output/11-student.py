#!/usr/bin/python3
"""This is a Python script that defines a Student class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with
        first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.
        """
        if attrs is None:
            attrs = []
        if not isinstance(attrs, list):
            raise TypeError("attrs must be a list of strings")
        student_dict = {}
        if not attrs:
            student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
        return student_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary representation of a Student instance.
        """
        if not isinstance(json, dict):
            raise TypeError("json must be a dictionary")
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
