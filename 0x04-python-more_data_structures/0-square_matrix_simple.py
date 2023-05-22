#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    t = map(lambda row: list(map(lambda n: n ** 2, row)), matrix)
    return list(t)
