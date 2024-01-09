#!/usr/bin/python3
import json
"""Defines fuction that serialize python data structure with json
"""


def to_json_string(my_obj):
    """serialize the data structure with json"""
    with open(my_obj, encoding='utf-8') as f:
        return json.dumps(my_obj)
