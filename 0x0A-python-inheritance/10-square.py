#!/usr/bin/python3

"""
Module of class Square that inherits from Rectangle class.
"""

# Import Rectangle class from module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Constructor for Square class that initializes private attributes.

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size):
        """
        Initialize the Square object with size.

        Args:
            size (int): size of the square
        """
        # Call integer_validator method from Rectangle to validate size
        self.integer_validator("size", size)
        # Initialize private attribute __size
        self.__size = size
        # Call super() to initialize width and height of Rectangle with size
        super().__init__(size, size)
