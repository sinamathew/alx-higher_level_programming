#!/usr/bin/python3

# Import the add function from add_0.py
from add_0 import add

# Define variables a and b
a = 1
b = 2

# Call add and display the result using string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
