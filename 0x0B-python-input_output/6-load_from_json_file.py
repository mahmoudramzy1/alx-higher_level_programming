#!/usr/bin/python3
"""Defines function that loads from json file"""


def load_from_json_file(filename):
    """loads from json file"""
    with open(filename, encoding='utf-8') as a:
        json.load(a)
