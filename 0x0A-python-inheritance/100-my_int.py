#!/usr/bin/python3
"""Defines a Rebel Class."""


class MyInt(int):
    """Defines a class MyInt."""
    def __init___(self, value):
        """Initialize.
        Args:
            value (int): An integer to rebel against.
        """
        super().__init__()

    def __eq__(self, other):
        """Defines equality.
        Args:
            other (int): Dont know yet
        Returns:
            Negative value
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines negativity.
        Args:
            other (int): Dont know yet
        Returns:
            Positive value.
        """
        return super().__eq__(other)
