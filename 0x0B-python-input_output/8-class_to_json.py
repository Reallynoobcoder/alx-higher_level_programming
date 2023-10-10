#!/usr/bin/python3
"""defines python class to json function"""


def class_to_json(obj):
    """a function that returns the dictionary description
        with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an objec
    """
    return obj.__dict__
