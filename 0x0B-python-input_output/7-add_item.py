#!/usr/bin/python3
"""
adds all arguments to a Python list,
and then save them to a file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if __name__ == "__main__":
    try:
        object = load_from_json_file(filename)
    except FileNotFoundError:
        object = []

    for add_list in sys.argv[1:]:
        object.append(add_list)
    save_to_json_file(object, filename)
