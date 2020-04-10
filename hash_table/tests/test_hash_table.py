import unittest

from _base import StructureTestsBase
from hash_table import HashTable


class HTTestsBase(StructureTestsBase):

    _TEST_CLS = HashTable
    _ARRAY_CLS = list
    _FILL_METHOD = 'put'

