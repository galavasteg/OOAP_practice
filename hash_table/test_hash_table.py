import unittest

from hash_table import HashTable


class HTTestsBase(unittest.TestCase):

    HT_SIZE = None
    INIT_ITEMS = None

    def setUp(self):
        if not all(map(None.__ne__, (self.HT_SIZE, self.INIT_ITEMS))):
            raise AttributeError('Set attributes: HT_SIZE, INIT_ITEMS')

        ht = HashTable(self.HT_SIZE)

        for v in self.INIT_ITEMS:
            ht.put(v)

        self.ht = ht

