#!/usr/bin/python3
"""Accept argument and add them into a python list, saving them to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    johnson = load_from_json_file("add_item.json")
except FileNotFoundError:
    johnson = []

for i in sys.argv[1:]:
    johnson.append(i)

save_to_json_file(johnson, 'add_item.json')
