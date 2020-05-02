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

    def __init__(self):
        """
        Initializing the instance after it's been created.

        """
        self._keys = DynamicArray()
        self._values = DynamicArray()
        self._size = 0
        self._capacity = self._keys.get_capacity()
        for i in range(self._capacity):
            self._keys.insert(i, ())
            self._values.insert(i, ())
