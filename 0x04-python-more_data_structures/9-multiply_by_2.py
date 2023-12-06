#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict()
    for i, n in a_dictionary.items():
        new[i] = n * 2
    return new
