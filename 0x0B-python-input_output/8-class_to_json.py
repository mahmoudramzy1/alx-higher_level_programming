#!/usr/bin/pyhton3
"""Defines function that returns dictaionary discribtion"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
