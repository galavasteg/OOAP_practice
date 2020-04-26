import unittest

from native_dictionary import Dictionary


class DictTestsBase(unittest.TestCase):

    INIT_ITEMS = None

    def setUp(self):
        if self.INIT_ITEMS is None:
            raise AttributeError('Set INIT_ITEMS')

        d = Dictionary()

        for k, v in self.INIT_ITEMS:
            d[k] = v

        self.dict = d
