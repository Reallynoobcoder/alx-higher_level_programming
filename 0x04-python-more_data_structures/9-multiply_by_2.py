#!/usr/bin/python3
def multiply_by_2(a_dictionary):
  multi_values = list(a_dictionary.values())
  for value in multi_values:
    value *= 2
  return multi_values
