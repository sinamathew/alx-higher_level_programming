#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("{:d} / {:d} = {:d}".format(a, b, result))
    return result
