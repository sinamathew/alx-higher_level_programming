#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        if (num != search):
            new_list.append(num)
        else:
            new_list.append(replace)
    return new_list
