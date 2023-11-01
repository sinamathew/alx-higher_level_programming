#!/usr/bin/python3
class LockedClass:
    """A class with no class or object attribute.

    Prevents the user from dynamically creating new instances attribute.

    """


    __slots__ = ('first_name')
    def __init__(self, first_name):
        """Accepts only one attribute.

        Exception is called while dynamically creating new attribute.
        
        """
        self.first_name = first_name
