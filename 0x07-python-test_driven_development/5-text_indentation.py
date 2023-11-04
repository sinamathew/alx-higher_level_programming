#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    v = 0
    while v < len(text) and text[v] == ' ':
        v += 1

    while v < len(text):
        print(text[v], end="")
        if text[v] == "\n" or text[v] in ".?:":
            if text[v] in ".?:":
                print("\n")
            v += 1
            while v < len(text) and text[v] == ' ':
                v += 1
            continue
        v += 1
