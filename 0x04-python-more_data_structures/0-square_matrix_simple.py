#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = [[element ** 2 for element in row] for row in matrix]
    return squared_matrix

