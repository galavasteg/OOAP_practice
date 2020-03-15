from collections.abc import Iterable
from random import choice
import unittest

from queues import Queue
class QueueTestsBase(unittest.TestCase):

    QUEUE_CLS = Queue
    INIT_ITEMS = range(0)

    def setUp(self):
        self.queue = self.QUEUE_CLS()
        self.queue = self.get_filled_queue(self.INIT_ITEMS)

    @classmethod
    def get_filled_queue(cls, items: Iterable) -> QUEUE_CLS:
        queue = cls.QUEUE_CLS()
        for v in items:
            queue.enqueue(v)
        return queue

    def check_items_after_enqueue(self, queue: QUEUE_CLS,
                                  ins_item: object):
        ins_index = len(queue)
        expected_items = (tuple(self.INIT_ITEMS[:ins_index]) + (ins_item,))

        self.assertEqual(len(queue), len(expected_items))

    def check_items_after_ok_dequeue(self, queue: QUEUE_CLS):
        del_index = 0
        expected_items = tuple(self.INIT_ITEMS[del_index + 1:])

        self.assertEqual(len(queue), len(expected_items))
        self.assertEqual(queue.get_dequeue_status(),
                         self.QUEUE_CLS.DEQUEUE_OK)

    def check_items_after_failed_dequeue(self, queue: QUEUE_CLS):
        expected_items = tuple(self.INIT_ITEMS)

        self.assertEqual(len(queue), len(expected_items))
        self.assertEqual(queue.get_dequeue_status(),
                         self.QUEUE_CLS.DEQUEUE_EMPTY_ERR)


class Queue1EmptyTests(QueueTestsBase):

    INIT_ITEMS = range(0)

    def test_01_constructor(self):
        _ = self.queue

        actual_params = (len(_), )
        actual_statuses = (
                _.get_dequeue_status(),
                _.get_peek_status(),
            )
        actual_state = actual_params + actual_statuses

        methods_init_status = init_size = 0
        expected_state = ((init_size, ) +
                          (methods_init_status,) * len(actual_statuses))

        self.assertTupleEqual(actual_state, expected_state)

    def test_02_empty_enqueue(self):
        self.queue.enqueue('item')

        self.check_items_after_enqueue(self.queue, 'item')

    def test_03_empty_peek_bad_empty(self):
        _ = self.queue.peek()

        self.assertEqual(self.queue.get_peek_status(),
                         self.QUEUE_CLS.PEEK_EMPTY_ERR)

    def test_04_empty_dequeue_bad_empty(self):
        self.queue.dequeue()

        self.check_items_after_failed_dequeue(self.queue)


class Queue2FilledTests(QueueTestsBase):

    INIT_ITEMS = range(8)

        item = self.queue.peek()

        self.assertEqual(self.queue.get_peek_status(),
                         self.QUEUE_CLS.PEEK_OK)

    def test_02_filled_dequeue(self):
        self.queue.dequeue()

        self.check_items_after_ok_dequeue(self.queue)


class Queue3DequeAllTests(QueueTestsBase):

    INIT_ITEMS = range(10000)

    def test_01_dequeue_all(self):
        for _ in range(len(self.INIT_ITEMS)):
            self.queue.dequeue()


        expected_size = 0
        self.assertEqual(len(self.queue), expected_size)
        self.assertEqual(self.queue.get_dequeue_status(),
                         self.QUEUE_CLS.DEQUEUE_OK)


if __name__ == '__main__':
    unittest.main()

