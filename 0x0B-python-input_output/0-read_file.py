#!/usr/bin/python3
# 0-read_file.py
"""module with a function that reads a file"""


def read_file(filename=""):
    """defining function"""

    with open(filename, "r", encoding="utf-8") as doc:
        for line in doc:
            print(line, end="")

        """
        content = doc.read()
        print(content)
        """
