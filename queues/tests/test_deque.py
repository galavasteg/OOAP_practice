from random import choice
import unittest

from _base import StructureTestsBase
from queues import Deque
from dynamic_array import DynamicArray


class DequeTestsBase(StructureTestsBase):

    _TEST_CLS = Deque
    _ARRAY_CLS = DynamicArray
    _FILL_METHOD = 'add_tail'

    def check_items_after_add_or_remove(self, expected_items: tuple):
        array = self.struct_inst._queue
        actual_items = self.get_array_items(array)

        self.assertTupleEqual(actual_items, expected_items)


class Deque1EmptyTests(DequeTestsBase):

    INIT_ITEMS = range(0)

    def test_01_constructor(self):
        deque = self.struct_inst

        actual_params = (len(deque), )
        actual_statuses = (
                deque.get_remove_status(),
                deque.get_get_status(),
            )
        actual_state = actual_params + actual_statuses

        methods_init_status, init_size = self._TEST_CLS.GET_NIL, 0
        expected_params = (init_size, )
        expected_statuses = (methods_init_status,) * len(actual_statuses)
        expected_state = expected_params + expected_statuses

        self.assertTupleEqual(actual_state, expected_state)

    def test_02_empty_add_front(self):
        self.struct_inst.add_front('item')

        expected_items = ('item',)
        self.check_items_after_add_or_remove(expected_items)

    def test_03_empty_add_tail(self):
        self.struct_inst.add_tail('item')

        expected_items = ('item',)
        self.check_items_after_add_or_remove(expected_items)

    def test_04_empty_remove_front_neg_empty(self):
        self.struct_inst.remove_front()

        expected_items = ()
        self.check_items_after_add_or_remove(expected_items)
        self.assertEqual(self.struct_inst.get_remove_status(),
                         self._TEST_CLS.REMOVE_EMPTY_ERR)

    def test_05_empty_remove_tail_neg_empty(self):
        self.struct_inst.remove_tail()

        expected_items = ()
        self.check_items_after_add_or_remove(expected_items)
        self.assertEqual(self.struct_inst.get_remove_status(),
                         self._TEST_CLS.REMOVE_EMPTY_ERR)

    def test_06_empty_get_front_neg_empty(self):
        _ = self.struct_inst.get_front()

        self.assertEqual(self.struct_inst.get_get_status(),
                         self._TEST_CLS.GET_EMPTY_ERR)

    def test_07_filled_get_tail_neg_empty(self):
        _ = self.struct_inst.get_tail()

        self.assertEqual(self.struct_inst.get_get_status(),
                         self._TEST_CLS.GET_EMPTY_ERR)


class Deque2FilledTests(DequeTestsBase):

    INIT_ITEMS = range(8)

    def test_01_filled_add_front(self):
        self.struct_inst.add_front('item')

        expected_items = ('item',) + tuple(self.INIT_ITEMS)
        self.check_items_after_add_or_remove(expected_items)

    def test_02_filled_add_tail(self):
        self.struct_inst.add_tail('item')

        expected_items = tuple(self.INIT_ITEMS) + ('item',)
        self.check_items_after_add_or_remove(expected_items)

    def test_03_filled_remove_front(self):
        self.struct_inst.remove_front()

        expected_items = tuple(self.INIT_ITEMS[1:])
        self.check_items_after_add_or_remove(expected_items)
        self.assertEqual(self.struct_inst.get_remove_status(),
                         self._TEST_CLS.REMOVE_OK)

    def test_04_filled_remove_tail(self):
        self.struct_inst.remove_tail()

        expected_items = tuple(self.INIT_ITEMS[:-1])
        self.check_items_after_add_or_remove(expected_items)
        self.assertEqual(self.struct_inst.get_remove_status(),
                         self._TEST_CLS.REMOVE_OK)

    def test_05_filled_get_front(self):
        actual_item = self.struct_inst.get_front()

        self.assertEqual(actual_item, self.INIT_ITEMS[0])
        self.assertEqual(self.struct_inst.get_get_status(),
                         self._TEST_CLS.GET_OK)

    def test_06_filled_get_tail(self):
        actual_item = self.struct_inst.get_tail()

        self.assertEqual(actual_item, self.INIT_ITEMS[-1])
        self.assertEqual(self.struct_inst.get_get_status(),
                         self._TEST_CLS.GET_OK)


class Deque3DequeAllTests(DequeTestsBase):

    INIT_ITEMS = range(10000)

    def test_01_remove_all_randomly(self):
        deque = self.struct_inst
        methods = (
                deque.remove_front.__name__,
                deque.remove_tail.__name__,
            )

        for _ in range(len(self.INIT_ITEMS)):
            method = choice(methods)
            deque.__getattribute__(method)()

        expected_items = ()
        self.check_items_after_add_or_remove(expected_items)
        self.assertEqual(len(deque), 0)
        self.assertEqual(deque.get_remove_status(),
                         self._TEST_CLS.REMOVE_OK)


if __name__ == '__main__':
    unittest.main()
