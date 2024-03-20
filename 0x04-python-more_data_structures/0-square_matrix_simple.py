#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[elemnt ** 2 for elemnt in row] for row in matrix]
    return new_matrix
