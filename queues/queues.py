"""
-------------------- 1. Queue ATD --------------------

This is an abstract data type specification for
a Queue implementation.

CONSTANTS

    GET_NIL        # get_front() not called yet
    GET_OK         # last get_front() call returned correct item
    GET_EMPTY_ERR  # queue is empty

    REMOVE_NIL        # dequeue() not called yet
    REMOVE_OK         # last dequeue() call completed successfully
    REMOVE_EMPTY_ERR  # queue is empty

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


-------------------- 2. Deque ATD --------------------

This is an abstract data type specification for
a Deque implementation.

CONSTANTS

    GET_NIL        # get_front/get_tail() not called yet
    GET_OK         # last get_front/get_tail() call returned correct item
    GET_EMPTY_ERR  # deque is empty

    REMOVE_NIL        # dequeue/remove_tail() not called yet
    REMOVE_OK         # last dequeue/remove_tail() call completed successfully
    REMOVE_EMPTY_ERR  # deque is empty

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

    enqueue(self, item: object) - Insert **item** into tail.

        Post-condition:
            - item added to deque tail.

    dequeue(self) - Delete the head-item from the deque.

        Pre-condition:
            - the deque is not empty.
        Post-condition:
            - the head-item removed from the deque.

    add_front(self, item: object) - Insert **item** into head.

        Post-condition:
            - item added to deque head.

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
    get_remove_status(self) -> status of last dequeue/remove_tail() call (REMOVE_* constant)

"""

from dynamic_array import DynamicArray


class __BaseQueue:

    GET_NIL = 0        # get_front/get_tail() not called yet
    GET_OK = 1         # last get_front/get_tail() call returned correct item
    GET_EMPTY_ERR = 2  # queue/deque is empty

    REMOVE_NIL = 0        # dequeue/remove_tail() not called yet
    REMOVE_OK = 1         # last dequeue/remove_tail() call completed successfully
    REMOVE_EMPTY_ERR = 2  # queue/deque is empty

    def __init__(self):
        """
        Initializing the instance after it's been created

        Post-condition:
            - the queue/deque command statuses set to
              initial (*_NIL constants).
            - the queue/deque size is 0.

        """
        super().__init__()
        self._queue = DynamicArray()

        self._get_status = self.GET_NIL
        self._remove_status = self.REMOVE_NIL

    # additional commands:
    def _remove_item_by_index(self, item_index: int):
        if len(self) == 0:
            self._remove_status = self.REMOVE_EMPTY_ERR
        else:

            self._queue.delete(item_index)

            self._remove_status = self.REMOVE_OK

    # commands:
    def enqueue(self, item):
        """
        Insert **item** into tail.

        Post-condition:
            - item added to queue/deque tail.

        """
        new_tail_index = len(self)
        self._queue.insert(new_tail_index, item)

    def dequeue(self):
        """
        Delete the head-item from the queue/deque.

        Pre-condition:
            - the queue/deque is not empty.
        Post-condition:
            - the head-item removed from the queue/deque.

        """
        head_i = 0
        self._remove_item_by_index(head_i)

    # additional requests:
    def _get_item_by_index(self, item_index: int) -> object:
        if len(self) == 0:
            self._get_status = self.GET_EMPTY_ERR

            item = None
        else:
            item = self._queue[item_index]

            self._get_status = self.GET_OK

        return item

    # requests:
    def __len__(self):
        """Return the number of items in the queue/deque."""
        return len(self._queue)

    def get_front(self) -> object:
        """
        Return the head-item of the queue/deque.

        Pre-condition:
            - the queue/deque is not empty.

        """
        head_i = 0
        item = self._get_item_by_index(head_i)
        return item

    # method statuses requests:
    def get_get_status(self) -> int:
        """Return status of last get_front/get_tail() call:
        one of the GET_* constants."""
        return self._get_status

    def get_remove_status(self) -> int:
        """Return status of last dequeue/remove_tail() call:
        one of the REMOVE_* constants."""
        return self._remove_status


class Queue(__BaseQueue):
    ...


class Deque(__BaseQueue):

    # commands:
    def add_front(self, item):
        """
        Insert **item** into head.

        Post-condition:
            - item added to deque head.

        """
        head_i = 0
        self._queue.insert(head_i, item)

    def remove_tail(self):
        """
        Delete the tail-item from the deque.

        Pre-condition:
            - the deque is not empty.
        Post-condition:
            - the tail-item removed from the deque.

        """
        tail_i = len(self) - 1
        self._remove_item_by_index(tail_i)

    # requests:
    def get_tail(self) -> object:
        """
        Return the tail-item of the deque.

        Pre-condition:
            - the deque is not empty.

        """
        tail_i = len(self) - 1
        item = self._get_item_by_index(tail_i)
        return item
