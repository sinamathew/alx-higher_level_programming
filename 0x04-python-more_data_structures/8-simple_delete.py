#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary
    if key:
        del new_dict[key]
    return new_dict
