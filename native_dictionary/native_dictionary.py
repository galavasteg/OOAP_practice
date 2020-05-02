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

import base64


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

    # additional requests
    def __iter__(self):
        """Iterate keys."""
        return self.keys()

    def keys(self):
        """Iterate keys."""
        for sub_keys in self._keys:
            if sub_keys:
                for k in sub_keys:
                    yield k

    def items(self):
        """Iterate items."""
        for sub_keys, sub_vals in zip(self._keys, self._values):
            if sub_keys:
                for item in zip(sub_keys, sub_vals):
                    yield item

    def is_key(self, key: str) -> bool:
        """Check if the **key** is in the dictionary."""
        hash_slot = self._hash_func(key)
        slot_keys = self._keys[hash_slot]
        is_key = key in slot_keys
        return is_key

    # requests:
    def __len__(self) -> int:
        """Get the number of items in the dictionary."""
        return self._items_count

    def __getitem__(self, key: str) -> object:
        """
        Get the item value by item **key**.

        Pre-condition:
            - **key** exists in the dictionary.

        """
        hash_slot = self._hash_func(key)
        subkeys = self._keys[hash_slot]

        if key not in subkeys:
            self._getitem_status = self.GETITEM_KEY_ERR
            return None

        subslot = subkeys.index(key)
        value = self._values[hash_slot][subslot]

        self._getitem_status = self.GETITEM_OK

        return value

    def _hash_func(self, key: str) -> int:
        """Compute **key** slot"""
        b_string = key.encode()
        hash_string = base64.encodebytes(b_string)[:-1]  # exclude last '/n'
        slot = sum(hash_string) % self._capacity
        return slot

    # method statuses requests:
    def get_getitem_status(self) -> int:
        """Return status of last __getitem__() call:
        one of the GETITEM_* constants."""
        return self._getitem_status

    def get_remove_status(self) -> int:
        """Return status of last remove() call:
        one of the REMOVE_* constants."""
        return self._remove_status
