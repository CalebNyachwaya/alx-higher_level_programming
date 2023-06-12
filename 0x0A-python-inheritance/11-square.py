#!/usr/bin/python3
""" This module defines the Square class """

# Import the Rectangle class from the '9-rectangle' module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class representing a square, inheriting from Rectangle """

    def __init__(self, size):
        """ Constructor that initializes private attributes

        Args:
            size (int): size of the square

        Attributes:
            __size (int): size of the square, private
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call parent class constructor

    def __str__(self):
        """ String representation of the Square object

        Returns:
            str: formatted string with square size
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
