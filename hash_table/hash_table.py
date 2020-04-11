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

    PUT_NIL = 0
    PUT_OK = 1
    PUT_FULL_ERR = 2
    PUT_EXISTS_ERR = 3
    PUT_COLLISION_ERR = 4

    def __init__(self, capacity: int):
        """

        """
        self._capacity = capacity
        self._values = [None] * self._capacity

        self._put_status = self.PUT_NIL

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
            - the hashtable is not full
            - **value** does not exist in hashtable
            - no collision resolution error
        Post-condition:
            - **value** added to hashtable.

        """
        if len(self) >= self._capacity:
            self._put_status = self.PUT_FULL_ERR
        else:

            hash_slot = self._hash_func(value)
            for slot in self._slots_stepper(hash_slot):

                if self._values[slot] == value:
                    self._put_status = self.PUT_EXISTS_ERR
                    break

                is_free = self._values[slot] is None
                if is_free:
                    self._values[slot] = value
                    self._put_status = self.PUT_OK

                else:
                    self._put_status = self.PUT_COLLISION_ERR


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
    def get_put_status(self) -> int:
        """Return status of last put() call:
        one of the PUT_* constants."""
        return self._put_status

