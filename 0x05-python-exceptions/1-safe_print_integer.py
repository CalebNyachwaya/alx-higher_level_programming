#!/bin/bash/python3

def safe_print_integer(value):
    try:
        print("{}".format(value + 0))
        return True
    except TypeError:
        return False
