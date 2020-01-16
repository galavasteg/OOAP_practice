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

CONSTRUCTOR
    __new__(cls, max_size: int) -> new bounded-stack instance
        Post-condition:
            created a new empty bounded-stack instance.

        NOTE: __new__ is NOT abstract method. You shouldn't
            need to override __new__. See:
            https://mail.python.org/pipermail/tutor/2008-April/061426.html

    __init__(self, max_size: int):
        Initializing the instance after it's been created.
        Post-condition:
            The stack storage capacity is limited to *max_size* number of items

COMMANDS
    push(self, value)
        Pre-condition:
            stack storage is not full.
        Post-condition:
            new item added into stack storage.

    pop(self)
        Pre-condition:
            stack storage is not empty.
        Post-condition:
            last added item removed from stack storage.

    clear(self)
        Post-condition:
            stack storage is empty.

"""

from abc import ABCMeta, abstractmethod


class AbstractBoundedStack(metaclass=ABCMeta):
    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct item
    PEEK_ERR = 2  # stack storage is empty

    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PUSH_NIL = 0  # push() not called yet
    PUSH_OK = 1   # last push() call returned correct item
    PUSH_ERR = 2  # stack storage is full

    # constructor
    def __new__(cls, *args) -> object:
        """
        Create a class instance
        Post-condition:
            created a new empty stack instance

        NOTE: __new__ is NOT abstract method. You shouldn't
            need to override __new__. See:
            https://mail.python.org/pipermail/tutor/2008-April/061426.html
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self, max_size: int):
        """Initializing the instance after it's been created"""

    # commands
    @abstractmethod
    def push(self, value: object):
        """
        Pre-condition: stack storage is not full.
        Post-condition: new item added into stack storage.
        """

    @abstractmethod
    def pop(self):
        """
        Pre-condition: stack storage is not empty.
        Post-condition: last added item removed from stack storage.
        """

    @abstractmethod
    def clear(self):
        """Post-condition: stack storage is empty."""


