#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        curr_row = []
        for x in row:
            curr_row.append(x * x)
        new_mat.append(curr_row)
    return new_mat
