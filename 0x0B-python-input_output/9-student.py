#!/usr/bin/python3
"""This is a module that defines a Student class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with
        first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return student_dict
