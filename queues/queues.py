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

    # additional commands:
    def _remove_item_by_index(self, item_index: int):
        if len(self) == 0:
            self._remove_status = self.REMOVE_EMPTY_ERR
        else:

            self._queue.delete(item_index)

            self._remove_status = self.REMOVE_OK

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
        return len(self._queue)

    def get_front(self) -> object:
        head_i = 0
        item = self._get_item_by_index(head_i)
        return item

    # method statuses requests:
    def get_get_status(self) -> int:
        return self._get_status

    def get_remove_status(self) -> int:
        return self._remove_status


class Queue(__BaseQueue, AbstractQueue):

    # commands:
    def enqueue(self, item):
        new_tail_index = len(self)
        self._queue.insert(new_tail_index, item)

    def dequeue(self):
        head_i = 0
        self._remove_item_by_index(head_i)


class Deque(__BaseQueue, AbstractDeque):

    # commands:
    def add_front(self, item):
        head_i = 0
        self._queue.insert(head_i, item)

    def add_tail(self, item):
        new_tail_index = len(self)
        self._queue.insert(new_tail_index, item)

    def remove_front(self):
        head_i = 0
        self._remove_item_by_index(head_i)

    def remove_tail(self):
        tail_i = len(self) - 1
        self._remove_item_by_index(tail_i)

    # requests:
    def get_tail(self) -> object:
        tail_i = len(self) - 1
        item = self._get_item_by_index(tail_i)
        return item
