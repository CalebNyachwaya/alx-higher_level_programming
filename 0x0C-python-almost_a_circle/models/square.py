#!/usr/bin/python3
""" import from Module rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor method that initializes size, x, y"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
