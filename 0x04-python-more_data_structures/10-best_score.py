#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    for key in a_dictionary:
        if a_dictionary[key] > best_key:
            best_key = a_dictionary[key]
    return best_key
