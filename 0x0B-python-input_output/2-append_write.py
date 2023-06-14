#!/usr/bin/python3
# 2-append_write.py

"""
a function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """function definition"""

    with open(filename, "a", encoding="utf-8") as doc:
        content = doc.write(text)
        return len(text)
