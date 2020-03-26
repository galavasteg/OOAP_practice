from .abstract_data_types import (
        _BaseAbstractQueue,
        AbstractQueue,
        AbstractDeque,
    )
from dynamic_array import DynamicArray


class __BaseQueue(_BaseAbstractQueue):

    def __init__(self):
        """Implementation of an AbstractQueue."""
        super().__init__()
        self._queue = DynamicArray()

        self._get_status = self.GET_NIL
        self._remove_status = self.REMOVE_NIL

    # requests:
    def __len__(self):
        return len(self._queue)

    def get_front(self) -> object:
        if len(self) == 0:
            self._get_status = self.GET_EMPTY_ERR

            item = super().get_front()
        else:
            head_i = 0
            item = self._queue[head_i]

            self._get_status = self.GET_OK

        return item

    # command statuses requests:
    def get_get_status(self) -> int:
        return self._get_status

    def get_remove_status(self) -> int:
        return self._remove_status


class Queue(__BaseQueue, AbstractQueue):

    # commands:
    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if len(self) == 0:
            self._remove_status = self.REMOVE_EMPTY_ERR
        else:
            head_i = 0

            self._queue.delete(head_i)

            self._remove_status = self.REMOVE_OK


class Deque(__BaseQueue, AbstractDeque):

    # commands:
    def add_front(self, item):
        self._queue.insert(0, item)

    def add_tail(self, item):
        self._queue.append(item)

    def remove_front(self):
        if len(self) == 0:
            self._remove_status = self.REMOVE_EMPTY_ERR
        else:
            head_i = 0

            self._queue.delete(head_i)

            self._remove_status = self.REMOVE_OK

    def remove_tail(self):
        if len(self) == 0:
            self._remove_status = self.REMOVE_EMPTY_ERR
        else:
            tail_i = len(self) - 1

            self._queue.delete(tail_i)

            self._remove_status = self.REMOVE_OK

    # requests:
    def get_tail(self) -> object:
        if len(self) == 0:
            self._get_status = self.GET_EMPTY_ERR

            item = super().get_tail()
        else:
            tail_i = len(self) - 1
            item = self._queue[tail_i]

            self._get_status = self.GET_OK

        return item
