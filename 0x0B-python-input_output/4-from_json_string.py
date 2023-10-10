#!/usr/bin/python3
"""Define a function that returns python from JSON string"""
import json


def from_json_string(my_str):
    """convert json string"""
    return json.loads(my_str)
