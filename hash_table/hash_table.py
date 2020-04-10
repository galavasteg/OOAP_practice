"""
This is an abstract data type specification for
a HashTable implementation.

CONSTANTS

CONSTRUCTOR

COMMANDS

REQUESTS

STATUS REQUESTS

"""


class HashTable:

    def __init__(self, size: int):
        """

        """
        self._size = size
        self._values = [None] * self._size

    def _hash_fun(self, value: str) -> int:
        bStr = value.encode()
        slot = sum(bStr) % self._size
        return slot

    def _slot_stepper(self, value):
        step = 1

        first_slot = tmp_slot = self._hash_fun(value)
        yield first_slot

        if self._values[first_slot] is not None:
            tmp_slot = (tmp_slot + step) % self._size
            yield tmp_slot

        while self._values[tmp_slot] is not None and first_slot != tmp_slot:
            tmp_slot = (tmp_slot + step) % self._size

            yield tmp_slot

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
    def get_size(self):
        return self._size

    # method statuses requests:
