#!/usr/bin/python3
"""Defining read file function"""


def read_file(filename=""):
    """Reads filename"""
    with open(filename, encoding="uft-8") as myfile:

        print(myfile.read(), end="")
