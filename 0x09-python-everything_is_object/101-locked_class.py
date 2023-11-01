#!/usr/bin/python3
class LockedClass:
    """A class with no class or object attribute.

    Prevents the user from dynamically creating new instances attribute.

    Attributes:
        __slots__ (tuple): A tuple containing the allowed attribute names.

    Note:
        Attempting to create or access attributes not listed in __slots__ will
            results in an AttributeError

    """

    __slots__ = ('first_name')
