"""
-------------------- AbstractDeque --------------------

AbstractDeque is an abstract data type for implementing
a deque

CONSTANTS

    GET_NIL = 0        # get_front/get_tail() not called yet
    GET_OK = 1         # last get_front/get_tail() call returned correct item
    GET_EMPTY_ERR = 2  # deque is empty

    REMOVE_NIL = 0        # remove_*() not called yet
    REMOVE_OK = 1         # last remove_*() call completed successfully
    REMOVE_EMPTY_ERR = 2  # deque is empty

CONSTRUCTOR

    __new__(cls) -> new deque instance
        Post-condition:
            - created a new instance.

    __init__(self, max_size: int):
        Initializing the instance after it's been created.

        Post-condition:
            - the deque method statuses set to initial (*_NIL constants)
            - the deque size is 0

COMMANDS

    add_front(self, item: object) - Insert **item** into head.

        Post-condition:
            - item added to deque head.

    remove_front(self) - Delete the head-item from the deque.

        Pre-condition:
            - the deque is not empty.
        Post-condition:
            - the head-item removed from the deque.

    add_tail(self, item: object) - Insert **item** into tail.

        Post-condition:
            - item added to deque tail.

    remove_tail(self) - Delete the tail-item from the deque.

        Pre-condition:
            - the deque is not empty.
        Post-condition:
            - the tail-item removed from the deque.

REQUESTS

    __len__(self) -> number of items in the deque

    get_front(self) -> the head-item of the deque

        Pre-condition:
            - the deque is not empty.

    get_tail(self) -> the tail-item of the deque

        Pre-condition:
            - the deque is not empty.

STATUS REQUESTS
    get_get_status(self) -> status of last get_front/get_tail() call (GET_* constant)
    get_remove_status(self) -> status of last remove_*() call (REMOVE_* constant)

"""

from abc import abstractmethod

from .abstract_queue import _BaseAbstractQueue


class AbstractDeque(_BaseAbstractQueue):

    # commands:
    @abstractmethod
    def add_front(self, item):
        """
        Insert **item** into head.

        Post-condition:
            - item added to deque head.

        """

    @abstractmethod
    def add_tail(self, item):
        """
        Insert **item** into tail.

        Post-condition:
            - item added to deque tail.

        """

    @abstractmethod
    def remove_front(self):
        """
        Delete the head-item from the deque.

        Pre-condition:
            - the deque is not empty.
        Post-condition:
            - the head-item removed from the deque.

        """

    @abstractmethod
    def remove_tail(self):
        """
        Delete the tail-item from the deque.

        Pre-condition:
            - the deque is not empty.
        Post-condition:
            - the tail-item removed from the deque.

        """

    # requests:
    @abstractmethod
    def get_tail(self) -> object:
        """Return the tail-item of the deque.

        Pre-condition:
            - the deque is not empty.

        """
        return None
