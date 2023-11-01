#!/usr/bin/python3
class LockedClass:
    """A class with no class or object attribute.

    Prevents the user from dynamically creating new instances attribute.

    Attributes:
        __slots__ (tuple): A tuple containing the allowed attribute names.

    Args:
        first_name (str): The value for th 'first_name' attribute.

    Note:
        Attempting to create or access attributes not listed in __slots__ will
            results in an AttributeError

    """

    __slots__ = ('first_name')

    def __init__(self, first_name):
        """Initialize the LockedClass instance.

        Args:
            first_name (str): the value for the 'first_name' attribute.

        Raises:
            AttributeError: if any attributes other than 'first_name' are
                accessed or created.

        """
        self.first_name = first_name
