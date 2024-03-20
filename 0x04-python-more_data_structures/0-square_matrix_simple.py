#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[integer ** 2 for integer in row] for row in matrix]
    return new_matrix
