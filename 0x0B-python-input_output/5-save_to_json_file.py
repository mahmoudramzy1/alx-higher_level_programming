#!/usr/bin/python3
"""Defines functions that writes text in file with json repr"""

import json


def save_to_json_file(my_obj, filename):
    """write my_obj in file with json repr"""

    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(obj, f)
