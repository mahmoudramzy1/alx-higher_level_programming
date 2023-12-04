#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in matrix:
            if len(row) == 0:
                print()
            for element in row:
                print("{:d}".format(element), end="\n" if row.index(element) == (len(row) - 1) else " ")
