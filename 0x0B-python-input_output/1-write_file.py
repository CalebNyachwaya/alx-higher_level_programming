#!/usr/bin/python3
# 1-write_file.py
"""
function that writes a string to a text file (UTFI)  and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """defining a function"""

    with open(filename,  "w", encoding="utf-8") as doc:
        doc.write(text)
        return len(text)
