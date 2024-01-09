#!/usr/bin/python3
"""Defines function that add arguements to list an save it in json file"""

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


arglist = list(sys.argv[1:])

try:
    old_data = 
