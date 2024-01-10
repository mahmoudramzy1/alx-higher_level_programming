#!/usr/bin/python3
"""Defines function that add arguements to list an save it in json file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file



try:
    json_list = load_from_json_file('add_item.json')
except  (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_to_json_file(json_list, 'add_item.json')
