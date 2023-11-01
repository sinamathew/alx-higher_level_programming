#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """A class with no class or object attribute.
    Prevents the user from dynamically creating new instances attribute.
    """

    __slots__ = ('first_name')
