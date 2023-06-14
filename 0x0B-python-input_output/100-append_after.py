#!/usr/bin/python3
"""
This module provides a functioni
for appending a line of text after each
line containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a
    specific string in a file.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
