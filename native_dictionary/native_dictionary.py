"""
This is an abstract data type specification for
a Dictionary implementation.

CONSTANTS

    SETITEM_NIL     # __setitem__() not called yet
    SETITEM_NEW     # last __setitem__() created a new item
    SETITEM_UPDATE  # last __setitem__() updated value of existing item

    REMOVE_NIL      # remove() not called yet
    REMOVE_OK       # last remove() call completed successfully
    REMOVE_KEY_ERR  # is no key of the dictionary

    GETITEM_NIL       # __getitem__() not called yet
    GETITEM_OK        # last __getitem__() returned correct value
    GETITEM_KEY_ERR   # in not key of the dictionary

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
        Put/update **key**-**value** item in the dictionary.

        Post-condition:
            - the item was placed/updated in the dictionary.

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

STATUS REQUESTS
    get_setitem_status(self) -> status of last __setitem__() call (SETITEM_* constant).
    get_remove_status(self) -> status of last remove() call (REMOVE_* constant).
    get_getitem_status(self) -> status of last __getitem__() call (GETITEM_* constant).

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

    # additional commands:
    def _resize(self, new_capacity: int):
        """Change the capacity and move existing items
        to the slots corresponding to the **new_capacity**."""
        items = tuple(self.items())

        self._capacity = new_capacity
        self._keys = [()] * self._capacity
        self._values = [()] * self._capacity
        self._items_count = 0
        self._busy_slots_count = 0
        for k, v in items:
            self.__setitem__(k, v)

    # commands:
    def __setitem__(self, key: str, value: object):
        """
        Put **key**-**value** item in the dictionary.

        Post-condition:
            - the item was placed in the dictionary.

        """
        hash_slot = self._hash_func(key)

        if (not self._keys[hash_slot]
                and self._busy_slots_count + 1 == self._capacity):
            new_capacity = self._capacity * self.CAPACITY_MULTIPLIER
            self._resize(new_capacity)

            hash_slot = self._hash_func(key)

        old_subkeys = self._keys[hash_slot]
        old_subvals = self._values[hash_slot]

        if not old_subkeys:  # set free slot
            sub_keys = (key,)
            sub_vals = (value,)
            self._busy_slots_count += 1
            self._items_count += 1
        elif key in old_subkeys:  # update existing key
            i = old_subkeys.index(key)
            sub_keys = old_subkeys
            sub_vals = old_subvals[:i] + (value,) + old_subvals[i + 1:]
        else:  # add a collision to sub-slots
            sub_keys = old_subkeys + (key,)
            sub_vals = old_subvals + (value,)
            self._items_count += 1

        self._keys[hash_slot] = sub_keys
        self._values[hash_slot] = sub_vals

    def remove(self, key: str):
        """
        Remove an item from the dictionary by the item **key**.

        Pre-condition:
            - **key** exists in the dictionary.
        Post-condition:
            - item removed from dictionary.

        """
        hash_slot = self._hash_func(key)

        if key not in self._keys[hash_slot]:
            self._remove_status = self.REMOVE_KEY_ERR
            return

        old_subkeys = self._keys[hash_slot]
        old_subvals = self._values[hash_slot]
        subslot = old_subkeys.index(key)

        sub_keys = old_subkeys[:subslot] + old_subkeys[subslot + 1:]
        sub_vals = old_subvals[:subslot] + old_subvals[subslot + 1:]
        self._keys[hash_slot] = sub_keys
        self._values[hash_slot] = sub_vals

        self._items_count -= 1

        if not sub_keys:  # free slot
            self._busy_slots_count -= 1
            fill_percent = self._busy_slots_count / self._capacity * 100
            shrink = (self._capacity > self.MIN_CAPACITY
                      and fill_percent < self.FILL_THRESHOLD_PERCENT)
            if shrink:

                new_capacity = int(self._capacity / self.CAPACITY_DELIMITER)
                if new_capacity < self.MIN_CAPACITY:
                    new_capacity = self.MIN_CAPACITY

                self._resize(new_capacity)

        self._remove_status = self.REMOVE_OK

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
