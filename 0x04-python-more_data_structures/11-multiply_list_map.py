#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiply = lambda x: x * number
    result = list(map(multiply, my_list))
    return result
