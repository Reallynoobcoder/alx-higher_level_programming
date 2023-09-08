#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    max_length = max(len(tuple_a), len(tuple_b))
    for i in range(max_length):
        element_a = tuple_a[i] if i < len(tuple_a) else 0
        element_b = tuple_b[i] if i < len(tuple_b) else 0
        result += (element_a + element_b,)
    return result
