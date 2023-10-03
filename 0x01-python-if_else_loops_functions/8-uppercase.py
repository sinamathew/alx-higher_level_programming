#!/usr/bin/python3
def uppercase(str):
    for cht in str:
        if ord(cht) >= 97 and ord(cht) <= 122:
            cht = chr(ord(cht) - 32)
        print("{:s}".format(cht), end='')

    print('\n', end="")
