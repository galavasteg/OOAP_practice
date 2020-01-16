"""
AbstractStack is an abstract data type for stack implementation.

CONSTANTS
    POP_NIL = 0   # pop() not called yet

    POP_OK = 1    # last pop() call completed successfully

    POP_ERR = 2   # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet

    PEEK_OK = 1   # last call peek() returned correct item

    PEEK_ERR = 2  # stack storage is empty

"""

from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):
    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct item
    PEEK_ERR = 2  # stack storage is empty


