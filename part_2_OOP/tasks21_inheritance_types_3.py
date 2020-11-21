"""
----------------------- TASK 21 -----------------------

    Приведите примеры кода, реализующие:
    1. наследование реализации (implementation inheritance),
    2. и льготное наследование (facility inheritance).

"""
from http import HTTPStatus
from typing import TypedDict
from unittest import TestCase


class HashTable:
    """Implementation: https://github.com/galavasteg/OOAP_practice/blob/master/part_1_ADT/hash_table/hash_table.py ."""
    def put(self, value): ...
    def remove(self, value): ...

    def __len__(self): ...
    def get_capacity(self): ...
    def is_value(self, value): ...


# 1. Implementation inheritance
class PowerSet(HashTable):
    """Implementation: https://github.com/galavasteg/OOAP_practice/blob/master/part_1_ADT/power_set.py ."""
    def intersection(self, with_set: 'PowerSet') -> 'PowerSet': ...
    def union(self, with_set: 'PowerSet') -> 'PowerSet': ...
    def difference(self, with_set: 'PowerSet') -> 'PowerSet': ...
    def is_subset(self, of_set: 'PowerSet') -> bool: ...


class SimpleResponse(TypedDict):
    result: dict
    meta: dict


class TestAPIMixin(object):

    NO_STATUS_CODE = -1

    def parse_response_code(self, response: SimpleResponse) -> int:
        code = response.get('meta', {}).get('status', self.NO_STATUS_CODE)
        return code


# 2. Facility inheritance
class BookAPITest(TestCase, TestAPIMixin):

    def test_get_book(self):
        response = ...
        self.assertEqual(self.parse_response_code(response), HTTPStatus.OK)
