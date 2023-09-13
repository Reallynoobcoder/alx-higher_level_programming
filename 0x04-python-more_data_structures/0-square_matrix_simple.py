#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        sqr = list(map(lambda a: a ** 2, row))
        result.append(sqr)
    return result
