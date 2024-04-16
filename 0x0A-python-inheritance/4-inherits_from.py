#!/usr/bin/python3
"""
===================================
module: method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """
    Method returns True if an object is an instance of a class
    that inherited from
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
