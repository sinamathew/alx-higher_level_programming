#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_result = ()
    for i in range(2):
        tuple_result[i] = tuple_a[i] + tuple_b[i]
    return tuple_result
