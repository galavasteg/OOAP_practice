import ctypes
from collections.abc import Iterable

from .abstract_data_types import (
        _BaseAbstractDynamicArray,
        AbstractDynamicArray,
    )


class _BaseDynamicArray(_BaseAbstractDynamicArray):

    INITIAL_CAPACITY = 16
    MIN_CAPACITY = INITIAL_CAPACITY
    CAPACITY_MULTIPLIER = 2
    CAPACITY_DELIMITER = 1.5
    DECREASE_CAPACITY_PERCENT_THRESHOLD = 50

    def __init__(self):
        """Implementation of an AbstractDynamicArray."""
        super().__init__()
        self.__size = 0
        self.__capacity = self.INITIAL_CAPACITY
        self.__array = self.__get_new_array(self.__capacity)

        self.__getitem_status = self.GETITEM_NIL
        self.__insert_status = self.GETITEM_NIL
        self.__delete_status = self.DELETE_NIL

    # commands:
    def insert(self, i: int, item):
        curr_size = len(self)
        capacity = self.get_capacity()

        resolved_i = i
        precondition_check = isinstance(i, int)
        if precondition_check:
            resolved_i = self._get_resolved_index(i)
            precondition_check = (resolved_i == curr_size
                                  or self._check_start_ind_bounds(resolved_i))
            if not precondition_check:
                self.__insert_status = self.INSERT_BOUNDS_ERR
        else:
            self.__insert_status = self.INSERT_TYPE_ERR

        if precondition_check:
            new_size = curr_size + 1
            next_items = self.__array[resolved_i:curr_size]
            if new_size > capacity:
                capacity = capacity * self.CAPACITY_MULTIPLIER

                prev_items = self.__array[:resolved_i]
                items = prev_items + [item] + next_items
                new_array = self.__get_new_array(capacity, items)
                self.__array = new_array
                self.__capacity = capacity
            else:
                self.__array[resolved_i:new_size] = [item] + next_items

            self.__size = new_size
            self.__insert_status = self.INSERT_OK

    def delete(self, i: int):
        curr_size = len(self)
        capacity = self.get_capacity()

        resolved_i = i
        precondition_check = isinstance(i, int)
        if precondition_check:
            resolved_i = self._get_resolved_index(i)
            precondition_check = self._check_start_ind_bounds(resolved_i)
            if not precondition_check:
                self.__delete_status = self.DELETE_BOUNDS_ERR
        else:
            self.__delete_status = self.DELETE_TYPE_ERR

        if precondition_check:
            new_size = curr_size - 1
            new_fill_percent = new_size / capacity * 100
            next_items = self.__array[resolved_i + 1:curr_size]
            decrease_capacity = (
                    capacity > self.MIN_CAPACITY
                    and new_fill_percent < self.DECREASE_CAPACITY_PERCENT_THRESHOLD)
            if decrease_capacity:
                new_capacity = int(capacity / self.CAPACITY_DELIMITER)
                if new_capacity < self.MIN_CAPACITY:
                    new_capacity = self.MIN_CAPACITY

                prev_items = self.__array[:resolved_i]
                items = prev_items + next_items
                new_array = self.__get_new_array(new_capacity, items)
                self.__array = new_array
                self.__capacity = new_capacity
            else:
                self.__array[resolved_i:new_size] = next_items

            self.__size = new_size
            self.__delete_status = self.DELETE_OK

    # additional commands:
    def append(self, item):
        i = len(self)
        self.insert(i, item)

    # requests:
    def __len__(self):
        return self.__size

    def __getitem__(self, i: int) -> object:
        if isinstance(i, int):
            resolved_i = self._get_resolved_index(i)
            if self._check_start_ind_bounds(resolved_i):

                item = self.__array[resolved_i]

                self.__getitem_status = self.GETITEM_OK
            else:
                item = None
                self.__getitem_status = self.GETITEM_OUT_OF_BOUNDS_ERR
        else:
            item = None
            self.__getitem_status = self.GETITEM_TYPE_ERR

        return item

    # additional requests:
    def __iter__(self):
        """TODO: tests"""
        for i in range(len(self)):
            yield self[i]

    def __get_new_array(self, capacity: int,
                        elements: Iterable = None) -> ctypes.Array:
        elements = elements or ()
        return (ctypes.py_object * capacity)(*elements)

    def get_capacity(self) -> int:
        return self.__capacity

    def _check_start_ind_bounds(self, i: int) -> bool:
        count = len(self)
        return count > 0 and 0 <= i < count

    def _get_resolved_index(self, i: int) -> int:
        # resolved_i, _, _ = slice(i, None).indices(len(self))
        resolved_i = i if i >= 0 else len(self) + i
        return resolved_i

    # command statuses requests:
    def get_getitem_status(self) -> int:
        return self.__getitem_status

    def get_insert_status(self) -> int:
        return self.__insert_status

    def get_delete_status(self) -> int:
        return self.__delete_status


class DynamicArray(AbstractDynamicArray, _BaseDynamicArray):
    ...

