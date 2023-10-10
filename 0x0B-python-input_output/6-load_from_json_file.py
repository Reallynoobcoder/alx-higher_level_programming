#!/usr/bin/python3
"""Define function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Add an object to json"""
    with open(filename, 'r') as file:
        return json.dumps(file.read())
