#!/usr/bin/python3
"""This is a module that defines a Student class."""


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
            attrs = []  # Initialize attrs with an empty list if not provided
        if not isinstance(attrs, list):
            raise TypeError("attrs must be a list of strings")
        student_dict = {}
        if not attrs:
            # If attrs is an empty list, retrieve all attributes
            student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            """ If attrs is a list of strings,
            retrieve only the specified attributes """
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
        return student_dict
