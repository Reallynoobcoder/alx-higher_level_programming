#!/usr/bin/python3
"""Define function that writes an Object to a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Writing to a JSON file using 'with'"""
    j_str = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(j_str)
