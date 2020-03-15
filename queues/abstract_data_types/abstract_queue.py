"""
AbstractQueue is an abstract data type for
implementing a queue.

CONSTANTS

    PEEK_NIL = 0        # peek() not called yet
    PEEK_OK = 1         # last peek() call returned correct item
    PEEK_EMPTY_ERR = 2  # queue is empty

    DEQUEUE_NIL = 0        # dequeue() not called yet
    DEQUEUE_OK = 1         # last dequeue() call completed successfully
    DEQUEUE_EMPTY_ERR = 2  # queue is empty

CONSTRUCTOR

    __new__(cls) -> new queue instance
        Post-condition:
            - created a new instance.

    __init__(self, max_size: int):
        Initializing the instance after it's been created.

        Post-condition:
            - the queue command statuses set to initial (*_NIL constants)
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
    peek(self) -> the head-item of the queue

STATUS REQUESTS
    get_peek_status(self) -> status of last peek() call (PEEK_* constant)
    get_dequeue_status(self) -> status of last dequeue() call (DEQUEUE_* constant)

"""

from abc import ABCMeta, abstractmethod


class AbstractQueue(metaclass=ABCMeta):

    PEEK_NIL = 0        # peek() not called yet
    PEEK_OK = 1         # last peek() call returned correct item
    PEEK_EMPTY_ERR = 2  # queue is empty

    DEQUEUE_NIL = 0        # dequeue() not called yet
    DEQUEUE_OK = 1         # last dequeue() call completed successfully
    DEQUEUE_EMPTY_ERR = 2  # queue is empty

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
            - the queue command statuses set to initial (*_NIL constants).
            - the queue size is 0.

        """

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

    # requests:
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return 0

    @abstractmethod
    def peek(self) -> object:
        """Return the head-item of the queue.

        Pre-condition:
            - the queue is not empty.

        """
        return None

    # method statuses requests:
    @abstractmethod
    def get_peek_status(self) -> int:
        """Return status of last peek() call:
        one of the PEEK_* constants."""
        return 0

    @abstractmethod
    def get_dequeue_status(self) -> int:
        """Return status of last dequeue() call:
        one of the DEQUEUE_* constants."""
        return 0

