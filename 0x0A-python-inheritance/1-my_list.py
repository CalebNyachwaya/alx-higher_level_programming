#!/usr/bin/python3
# 1-my_list.py
""" module showing inheritance """


class MyList(list):
    """class MyList inherits from list"""
    def print_sorted(self):
        goodList = sorted(self)
        print(goodList)
