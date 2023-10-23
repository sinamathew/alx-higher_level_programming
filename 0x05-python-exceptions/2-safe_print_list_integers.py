#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[1]), end="")
            i += 1
        except (ValueError, TypeError):
            break
    print()
    return i
