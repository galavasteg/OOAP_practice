"""
-------------------- AbstractQueue --------------------

AbstractQueue is an abstract data type for
implementing a queue.

CONSTANTS

    GET_NIL = 0        # get_front() not called yet
    GET_OK = 1         # last get_front() call returned correct item
    GET_EMPTY_ERR = 2  # queue is empty

    REMOVE_NIL = 0        # dequeue() not called yet
    REMOVE_OK = 1         # last dequeue() call completed successfully
    REMOVE_EMPTY_ERR = 2  # queue is empty

CONSTRUCTOR

    __new__(cls) -> new queue instance
        Post-condition:
            - created a new instance.

    __init__(self, max_size: int):
        Initializing the instance after it's been created.

        Post-condition:
            - the queue method statuses set to initial (*_NIL constants)
            - the queue size is 0

COMMANDS

    enqueue(self, item: object) - Insert **item** into tail.

        Post-condition:
            - item added to queue tail.

    dequeue(self) - Delete the head-item from the queue.

        Pre-condition:
            - the queue is not empty.
        Post-condition:
            - the head-item removed from the queue.

REQUESTS

    __len__(self) -> number of items in the queue

    get_front(self) -> the head-item of the queue

        Pre-condition:
            - the queue is not empty.

STATUS REQUESTS
    get_get_status(self) -> status of last get_front() call (GET_* constant)
    get_dequeue_status(self) -> status of last dequeue() call (REMOVE_* constant)

"""

from abc import ABCMeta, abstractmethod


class _BaseAbstractQueue(metaclass=ABCMeta):

    GET_NIL = 0        # get_front/get_tail() not called yet
    GET_OK = 1         # last get_front/get_tail() call returned correct item
    GET_EMPTY_ERR = 2  # queue/deque is empty

    REMOVE_NIL = 0        # dequeue/remove_*() not called yet
    REMOVE_OK = 1         # last dequeue/remove_*() call completed successfully
    REMOVE_EMPTY_ERR = 2  # queue/deque is empty

    # constructor
    def __new__(cls) -> object:
        """
        Create a class instance.
        Post-condition: created a new instance.
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """Initializing the instance after it's been created

        Post-condition:
            - the queue/deque command statuses set to
              initial (*_NIL constants).
            - the queue size is 0.

        """

    # requests:
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the queue/deque."""
        return 0

    @abstractmethod
    def get_front(self) -> object:
        """Return the head-item of the queue/deque.

        Pre-condition:
            - the queue/deque is not empty.

        """
        return None

    # method statuses requests:
    @abstractmethod
    def get_get_status(self) -> int:
        """Return status of last get_front/get_tail() call:
        one of the GET_* constants."""
        return 0

    @abstractmethod
    def get_remove_status(self) -> int:
        """Return status of last dequeue/remove_*() call:
        one of the REMOVE_* constants."""
        return 0


class AbstractQueue(_BaseAbstractQueue):

    # commands:
    @abstractmethod
    def enqueue(self, item):
        """Insert **item** into tail.

        Post-condition:
            - item added to queue tail.

        """

    @abstractmethod
    def dequeue(self):
        """Delete the head-item from the queue.

        Pre-condition:
            - the queue is not empty.
        Post-condition:
            - the head-item removed from the queue.

        """
