#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list[:].reverse()
    for i in range(len(reverse_list)):
        print("{:d}".format(reverse_list[i]))
