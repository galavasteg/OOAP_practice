"""
----------------------- TASK 21 -----------------------

    Приведите примеры кода, реализующие:
    1. наследование реализации (implementation inheritance),
    2. и льготное наследование (facility inheritance).

"""
from http import HTTPStatus
from typing import TypedDict
from unittest import TestCase


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
