#!/usr/bin/python3
'''import module json'''
import json


def from_json_string(my_str):
    '''
    Converts a JSON string to a Python object

    Args:
        my_str (str): The JSON string to be converted
    '''
    obj = json.loads(my_str)
    return obj
