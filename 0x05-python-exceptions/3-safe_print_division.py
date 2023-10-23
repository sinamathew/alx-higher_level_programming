#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    finally:
        print("{} / {} = {}".format(a, b, result))
    return result
