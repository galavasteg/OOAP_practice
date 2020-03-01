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

    # additional commands:

    # requests:

    # additional requests:

    # command statuses requests:
    def get_getitem_status(self) -> int:
        return self.__getitem_status

    def get_insert_status(self) -> int:
        return self.__insert_status

    def get_delete_status(self) -> int:
        return self.__delete_status


class DynamicArray(AbstractDynamicArray, _BaseDynamicArray):
    ...

