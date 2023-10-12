#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = 0
    for key in a_dictionary:
        best_key = a_dictionary[key] if a_dictionary[key] > best_key
    return best_key
