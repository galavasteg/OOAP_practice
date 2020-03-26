import unittest
from collections.abc import Iterable


class StructureTestsBase(unittest.TestCase):

    _TEST_CLS = None
    _ARRAY_CLS = None
    _FILL_METHOD = None

    INIT_ITEMS = range(0)

    def setUp(self):
        self.struct_inst = self._TEST_CLS()
        self.struct_inst = self.get_filled_structure(self.INIT_ITEMS)

    @classmethod
    def get_filled_structure(cls, items: Iterable) -> _TEST_CLS:
        struct = cls._TEST_CLS()
        fill_methods = struct.__getattribute__(cls._FILL_METHOD)
        for v in items:
            fill_methods(v)
        return struct

    @staticmethod
    def get_array_items(array: _ARRAY_CLS):
        items = tuple(map(lambda i: array[i], range(len(array))))
        return items
