"""

CONSTANTS

CONSTRUCTOR

COMMANDS

REQUESTS

STATUS REQUESTS

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
