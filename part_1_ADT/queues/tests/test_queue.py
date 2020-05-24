import unittest

from _base import StructureTestsBase
from part_1_ADT.queues import Queue
from part_1_ADT.dynamic_array import DynamicArray


class QueueTestsBase(StructureTestsBase):

    _TEST_CLS = Queue
    _ARRAY_CLS = DynamicArray
    _FILL_METHOD = 'add_tail'

    def check_items_after_enqueue(self, queue: _TEST_CLS,
                                  ins_item: object):
        array = queue._queue
        actual_items = self.get_array_items(array)

        ins_index = len(queue)
        expected_items = (tuple(self.INIT_ITEMS[:ins_index]) + (ins_item,))

        self.assertEqual(array[-1], ins_item)
        self.assertTupleEqual(actual_items, expected_items)
        self.assertEqual(len(queue), len(expected_items))

    def check_items_after_ok_dequeue(self, queue: _TEST_CLS):
        array = queue._queue
        actual_items = self.get_array_items(array)

        del_index = 0
        expected_items = tuple(self.INIT_ITEMS[del_index + 1:])

        self.assertTupleEqual(actual_items, expected_items)
        self.assertEqual(len(queue), len(expected_items))
        self.assertEqual(queue.get_remove_status(),
                         self._TEST_CLS.REMOVE_OK)

    def check_items_after_failed_dequeue(self, queue: _TEST_CLS):
        array = queue._queue
        actual_items = self.get_array_items(array)
        expected_items = tuple(self.INIT_ITEMS)

        self.assertTupleEqual(actual_items, expected_items)
        self.assertEqual(len(queue), len(expected_items))
        self.assertEqual(queue.get_remove_status(),
                         self._TEST_CLS.REMOVE_EMPTY_ERR)


class Queue1EmptyTests(QueueTestsBase):

    INIT_ITEMS = range(0)

    def test_01_constructor(self):
        _ = self.struct_inst

        actual_params = (len(_), )
        actual_statuses = (
                _.get_remove_status(),
                _.get_get_status(),
            )
        actual_state = actual_params + actual_statuses

        methods_init_status = init_size = 0
        expected_state = ((init_size, ) +
                          (methods_init_status,) * len(actual_statuses))

        self.assertTupleEqual(actual_state, expected_state)

    def test_02_empty_enqueue(self):
        self.struct_inst.add_tail('item')

        self.check_items_after_enqueue(self.struct_inst, 'item')

    def test_03_empty_get_front_bad_empty(self):
        _ = self.struct_inst.get_front()

        self.assertEqual(self.struct_inst.get_get_status(),
                         self._TEST_CLS.GET_EMPTY_ERR)

    def test_04_empty_dequeue_bad_empty(self):
        self.struct_inst.remove_front()

        self.check_items_after_failed_dequeue(self.struct_inst)


class Queue2FilledTests(QueueTestsBase):

    INIT_ITEMS = range(8)

    def test_01_filled_get_front(self):
        array = self.struct_inst._queue

        item = self.struct_inst.get_front()

        self.assertEqual(self.struct_inst.get_get_status(),
                         self._TEST_CLS.GET_OK)
        self.assertEqual(array[0], item)

    def test_02_filled_dequeue(self):
        self.struct_inst.remove_front()

        self.check_items_after_ok_dequeue(self.struct_inst)


class Queue3DequeAllTests(QueueTestsBase):

    INIT_ITEMS = range(10000)

    def test_01_dequeue_all(self):
        for _ in range(len(self.INIT_ITEMS)):
            self.struct_inst.remove_front()

        expected_items = ()
        array = self.struct_inst._queue
        actual_items = self.get_array_items(array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = 0
        self.assertEqual(len(self.struct_inst), expected_size)
        self.assertEqual(self.struct_inst.get_remove_status(),
                         self._TEST_CLS.REMOVE_OK)


if __name__ == '__main__':
    unittest.main()
