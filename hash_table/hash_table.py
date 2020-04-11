"""
This is an abstract data type specification for
a HashTable implementation.

CONSTANTS

CONSTRUCTOR

COMMANDS

REQUESTS

STATUS REQUESTS

"""

from typing import Generator


class HashTable:

    def __init__(self, capacity: int):
        """

        """
        self._capacity = capacity
        self._values = [None] * self._capacity


    # additional requests:
    def _hash_func(self, value: str) -> int:
        bStr = value.encode()
        slot = sum(bStr) % self._capacity
        return slot

    def _slots_stepper(self, start_slot: int) -> Generator[int]:

        yield start_slot

        is_collision = self._values[start_slot] is not None
        tmp_slot, step = start_slot, 1
        while is_collision and tmp_slot < self._capacity:
            tmp_slot += step

            yield tmp_slot

            is_collision = self._values[tmp_slot] is not None
            step = step ** 2

    # commands:
    def put(self, value: str):
        """
        Store **value** into hashtable.

        Pre-condition:
            - there is no collision
        Post-condition:
            - item added to queue/deque tail.

        """

    # requests:
    def __len__(self):
        return len(tuple(filter(None.__ne__, self._values)))

    def is_value(self, value: str) -> bool:
        is_value = False

        hash_slot = self._hash_func(value)
        for slot in self._slots_stepper(hash_slot):

            is_value = self._values[slot] == value
            if is_value:
                break

        return is_value

    def get_capacity(self):
        return self._capacity

    # method statuses requests:
