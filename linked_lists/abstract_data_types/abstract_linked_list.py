"""
AbstractLinkedList is an abstract data type for
implementing a linked list.

CONSTANTS
    HEAD_NIL = 0  # head() not called yet
    HEAD_OK = 1   # last head() call completed successfully
    HEAD_ERR = 2  # storage is empty

    TAIL_NIL = 0  # tail() not called yet
    TAIL_OK = 1   # last tail() call completed successfully
    TAIL_ERR = 2  # storage is empty

    RIGHT_NIL = 0        # right() not called yet
    RIGHT_OK = 1         # last right() call completed successfully
    RIGHT_EMPTY_ERR = 2  # storage is empty
    RIGHT_TAIL_ERR = 3   # cursor is on the last node

CONSTRUCTOR
    __new__(cls, max_size: int) -> new linked-list instance
        Post-condition:
            created a new instance with empty storage

    __init__(self, max_size: int):
        Initializing the instance after it's been created.
        Post-condition:
            The stack storage capacity is limited to *max_size* number
            of items

COMMANDS
    head(self) - Move cursor to the 1st node.
        Pre-condition:
            storage is not empty.
        Post-condition:
            cursor is on the 1st node.

    tail(self) - Move cursor to the last node.
        Pre-condition:
            storage is not empty.
        Post-condition:
            cursor is on the last node.

    right(self) - Move cursor to node right.
        Pre-conditions:
            - storage is not empty.
            - cursor is not on the last node;
        Post-condition:
            cursor is on the node to the right.

    put_right(self, value: object) - Put a new node with the *value* to
                                     the right of the node the cursor on.
        Pre-condition:
            storage is not empty.
        Post-condition:
            a new node with the *value* is in the storage to the right of
            the node the cursor on.

    put_left(self, value: object) - Put a new node with the *value* to
                                    the left of the node the cursor on.
        Pre-condition:
            storage is not empty.
        Post-condition:
            a new node with the *value*
            is in the storage to the left of
            the node the cursor on.

    def remove(self) - Remove the node the cursor on from the storage.
                       The cursor sets to the right (priority) or
                       to the left node if they exist.
        Pre-condition:
            storage is not empty.

REQUESTS
    get(self) -> value of the node the cursor on
        Pre-condition:
            storage is not empty.

    get_size(self) -> number of items in the storage

"""

from abc import ABCMeta, abstractmethod


class AbstractLinkedList(metaclass=ABCMeta):
    HEAD_NIL = 0  # head() not called yet
    HEAD_OK = 1   # last head() call completed successfully
    HEAD_ERR = 2  # storage is empty

    TAIL_NIL = 0  # tail() not called yet
    TAIL_OK = 1   # last tail() call completed successfully
    TAIL_ERR = 2  # storage is empty

    RIGHT_NIL = 0        # right() not called yet
    RIGHT_OK = 1         # last right() call completed successfully
    RIGHT_EMPTY_ERR = 2  # storage is empty
    RIGHT_TAIL_ERR = 3   # cursor is on the last node

    PUT_RIGHT_NIL = 0  # put_right() not called yet
    PUT_RIGHT_OK = 1   # last put_right() call completed successfully
    PUT_RIGHT_ERR = 2  # storage is empty

    PUT_LEFT_NIL = 0  # put_left() not called yet
    PUT_LEFT_OK = 1   # last put_left() call completed successfully
    PUT_LEFT_ERR = 2  # storage is empty

    REMOVE_NIL = 0  # remove() not called yet
    REMOVE_OK = 1   # last remove() call completed successfully
    REMOVE_ERR = 2  # storage is empty

    GET_NIL = 0  # get() not called yet
    GET_OK = 1   # last get() call returned correct item
    GET_ERR = 2  # storage is empty

    # constructor
    def __new__(cls) -> object:
        """
        Create a class instance
        Post-condition: created a new instance with empty storage
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """Initializing the instance after it's been created"""

    # commands
    @abstractmethod
    def head(self):
        """
        Move cursor to the 1st node.
        Pre-condition: storage is not empty.
        Post-condition: cursor is on the 1st node.
        """

    @abstractmethod
    def tail(self):
        """
        Move cursor to the last node.
        Pre-condition: storage is not empty.
        Post-condition: cursor is on the last node.
        """

    @abstractmethod
    def right(self):
        """
        Move cursor to node right.
        Pre-conditions:
            - storage is not empty.
            - cursor is not on the last node;
        Post-condition: cursor is on the node to the right.
        """

    @abstractmethod
    def put_right(self, value: object):
        """
        Put a new node with the *value* to the right
        of the node the cursor on.
        Pre-condition: storage is not empty.
        Post-condition: a new node with the *value*
            is in the storage to the right of
            the node the cursor on.
        """

    @abstractmethod
    def put_left(self, value: object):
        """
        Put a new node with the *value* to the left
        of the node the cursor on.
        Pre-condition: storage is not empty.
        Post-condition: a new node with the *value*
            is in the storage to the left of
            the node the cursor on.
        """

    @abstractmethod
    def remove(self):
        """
        Remove the node the cursor on from the storage.
        The cursor sets to the right (priority) or
        to the left node if they exist.
        Pre-condition: storage is not empty.
        """

    # requests:
    @abstractmethod
    def get(self) -> object:
        """
        Get the value of node the cursor on.
        Pre-condition: storage is not empty.
        """
        return 0

    @abstractmethod
    def get_size(self) -> int:
        """Return the number of items in the storage"""
        return 0

