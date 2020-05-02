"""
This is an abstract data type specification for
a Dictionary implementation.

CONSTANTS

    GETITEM_NIL       # __getitem__() not called yet
    GETITEM_OK        # last __getitem__() returned correct value
    GETITEM_KEY_ERR   # in not key of the dictionary

    REMOVE_NIL      # remove() not called yet
    REMOVE_OK       # last remove() call completed successfully
    REMOVE_KEY_ERR  # is no key of the dictionary

CONSTRUCTOR

    __new__(cls) -> new instance.
        Post-condition:
            - created a new instance.

    __init__(self, capacity: int):
        Initializing the instance after it's been created.

        Post-condition:
            - items count in the dictionary is 0.
            - method statuses set to initial (*_NIL constants).

COMMANDS

    __setitem__(self, key: str, value: object):
        Put **key**-**value** item in the dictionary.

        Post-condition:
            - the item was placed in the dictionary.

    remove(self, key: str):
        Remove an item from the dictionary by the item **key**.

        Pre-condition:
            - **key** exists in the dictionary.
        Post-condition:
            - item removed from dictionary.

REQUESTS

    __len__(self) -> number of items in the dictionary.

    __getitem__(self, key: str) -> item value.
        Pre-condition:
            - **key** exists in the dictionary.

    _hash_func(self, key: str) -> **key** slot.

STATUS REQUESTS
    get_getitem_status(self) -> status of last __getitem__() call (GETITEM_* constant).
    get_remove_status(self) -> status of last remove() call (REMOVE_* constant).

"""

from dynamic_array import DynamicArray


class Dictionary:

    GETITEM_NIL = 0       # __getitem__() not called yet
    GETITEM_OK = 1        # last __getitem__() returned correct value
    GETITEM_KEY_ERR = 2   # in not key of the dictionary

    REMOVE_NIL = 0      # remove() not called yet
    REMOVE_OK = 1       # last remove() call completed successfully
    REMOVE_KEY_ERR = 2  # is no key of the dictionary

    INITIAL_CAPACITY = 16

    # for resize in __setitem__()
    CAPACITY_MULTIPLIER = 2

    # for resize in remove()
    FILL_THRESHOLD_PERCENT = 50
    CAPACITY_DELIMITER = 1.5
    MIN_CAPACITY = 16

    def __init__(self):
        """
        Initializing the instance after it's been created.

        Post-condition:
            - items count in the dictionary is 0.
            - method statuses set to initial (*_NIL constants).

        """
        self._capacity = self.INITIAL_CAPACITY
        self._keys = [()] * self._capacity
        self._values = [()] * self._capacity
        self._items_count = 0
        self._busy_slots_count = 0

        self._getitem_status = self.GETITEM_NIL
        self._remove_status = self.REMOVE_NIL
