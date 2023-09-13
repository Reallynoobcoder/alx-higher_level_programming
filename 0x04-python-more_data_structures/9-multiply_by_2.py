#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_values = {}
    for key in a_dictionary:
        multi_values[key] = a_dictionary[key] * 2
    return multi_values
