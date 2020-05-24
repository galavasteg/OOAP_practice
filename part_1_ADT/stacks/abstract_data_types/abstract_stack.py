"""
AbstractStack is an abstract data type for stack implementation.

CONSTANTS
    POP_NIL = 0   # pop() not called yet

    POP_OK = 1    # last pop() call completed successfully

    POP_ERR = 2   # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet

    PEEK_OK = 1   # last call peek() returned correct item

    PEEK_ERR = 2  # stack storage is empty

CONSTRUCTOR
    __new__(cls) -> new stack instance
        Post-condition:
            created a new empty stack instance.

    __init__(self):
        Initializing the instance after it's been created.

COMMANDS
    push(self, value)
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

REQUESTS
    peek(self) -> last pushed item
        Pre-condition:
            stack storage is not empty.

    size(self) -> number of items in the stack storage

ADDITIONAL REQUESTS
    get_pop_status(self) -> status of last pop() call (POP_* constant)

    get_peek_status(self) -> status of last peek() call (PEEK_* constant)

"""

from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):
    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct item
    PEEK_ERR = 2  # stack storage is empty

    # constructor
    def __new__(cls) -> object:
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
    def __init__(self):
        """Initializing the instance after it's been created"""

    # commands
    @abstractmethod
    def push(self, value: object):
        """Post-condition: new item added into stack storage"""

    @abstractmethod
    def pop(self):
        """
        Pre-condition: stack storage is not empty.
        Post-condition: last added item removed from stack storage.
        """

    @abstractmethod
    def clear(self):
        """Post-condition: stack storage is empty."""

    # requests:
    @abstractmethod
    def peek(self) -> object:
        """
        Return last pushed item.
        Pre-condition: stack storage is not empty.
        """
        return 0

    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the stack storage"""
        return 0

    # additional requests:
    @abstractmethod
    def get_pop_status(self) -> int:
        """Return status of last pop() call:
        one of the POP_* constants"""

    @abstractmethod
    def get_peek_status(self) -> int:
        """Return status of last peek() call:
        one of the PEEK_* constants"""

