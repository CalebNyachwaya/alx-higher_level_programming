#!/usr/bin/python3
""" Class MyInt """


class MyInt(int):
    """ Class MyInt that overrides the equality operators """

    def __eq__(self, other):
        """ Override the equality operator (==)

        Args:
            other (Any): The object to compare with.
        """
        return False

    def __ne__(self, other):
        """ Override the inequality operator (!=)

        Args:
            other (Any): The object to compare with.
        """
        return True
