"""
AbstractBoundedStack is an abstract data type for
implementing a bounded-stack. The constructor of
the bounded-stack gets a positive integer -
the maximum possible number of items in the stack
storage.

CONSTANTS
    PEEK_NIL = 0  # peek() not called yet

    PEEK_OK = 1   # last call peek() returned correct item

    PEEK_ERR = 2  # stack storage is empty

    POP_NIL = 0   # pop() not called yet

    POP_OK = 1    # last pop() call completed successfully

    POP_ERR = 2   # stack storage is empty

    PUSH_NIL = 0  # push() not called yet

    PUSH_OK = 1   # last push() call returned correct item

    PUSH_ERR = 2  # stack storage is full

"""

from abc import ABCMeta, abstractmethod


class AbstractBoundedStack(metaclass=ABCMeta):
    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct item
    PEEK_ERR = 2  # stack storage is empty

    PUSH_NIL = 0  # push() not called yet
    PUSH_OK = 1   # last push() call returned correct item
    PUSH_ERR = 2  # stack storage is full


