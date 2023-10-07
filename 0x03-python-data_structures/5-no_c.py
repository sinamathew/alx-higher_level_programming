#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        del my_string[i] if 'C' or 'c'

    return my_string
