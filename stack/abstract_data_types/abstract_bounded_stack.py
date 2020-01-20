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

    __init__(self, max_size: int):
        Initializing the instance after it's been created.
        Post-condition:
            The stack storage capacity is limited to *max_size* number
            of items

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

REQUESTS
    peek(self) -> last pushed item
        Pre-condition: stack storage is not empty

    get_current_size(self) -> number of items in the stack storage

    get_max_size(self) -> maximum possible number of items in the stack
                          storage

ADDITIONAL REQUESTS
    get_peek_status(self) -> status of last peek() call (PEEK_* constant)

    get_pop_status(self) -> status of last pop() call (POP_* constant)

    get_push_status(self) -> status of last push() call (PUSH_* constant)

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

    # requests:
    @abstractmethod
    def peek(self) -> object:
        """
        Return last pushed item.
        Pre-condition: stack storage is not empty.
        """
        return 0

    @abstractmethod
    def get_current_size(self) -> int:
        """Return the number of items on the stack storage"""
        return 0

    @abstractmethod
    def get_max_size(self) -> int:
        """Return the maximum possible number
        of items in the stack storage"""
        return 0

    # additional requests:
    @abstractmethod
    def get_peek_status(self) -> int:
        """Return status of last peek() call:
        one of the PEEK_* constants"""
        return 0

    @abstractmethod
    def get_pop_status(self) -> int:
        """Return status of last pop() call:
        one of the POP_* constants"""
        return 0

    @abstractmethod
    def get_push_status(self) -> int:
        """Return status of last push() call:
        one of the PUSH_* constants"""
        return 0

