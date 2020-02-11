import unittest

from linked_lists.lists import LinkedList, TwoWayList


class __ParentListTestsMixin:
    linked_list_cls = None

    @classmethod
    def _get_filled_list(cls, *vals) -> linked_list_cls:
        linked_list = cls.linked_list_cls()
        for v in vals:
            linked_list.add_tail(v)
        return linked_list

    def _check_initial_state(self, list_: linked_list_cls):
        _ = list_
        actual_params = (_.get_size(), _.is_value(),
                         _.is_head(), _.is_tail(),)
        actual_statuses = (
                _.get_find_status(), _.get_get_status(),
                _.get_head_status(), _.get_put_left_status(),
                _.get_put_right_status(), _.get_remove_all_status(),
                _.get_remove_status(), _.get_replace_status(),
                _.get_right_status(), _.get_tail_status(),
            )
        actual_state = actual_params + actual_statuses

        methods_init_status = init_size = 0
        expected_state = ((init_size,) + (False,) * 3 +
                          (methods_init_status,) * len(actual_statuses))

        self.assertTupleEqual(actual_state, expected_state)

    def test_01_constructor(self):
        list_ = self.linked_list_cls()
        self._check_initial_state(list_)

    # commands tests
    def test_02_head(self):
        list_ = self.linked_list_cls()
        list_.head()
        self.assertEqual(list_.get_head_status(), self.linked_list_cls.HEAD_EMPTY_ERR)

        list_.add_tail('1st')
        list_.add_tail('last')
        list_.right()
        self.assertEqual(list_.get(), 'last')

        list_.head()
        self.assertEqual(list_.get(), '1st')
        self.assertEqual(list_.get_head_status(), self.linked_list_cls.HEAD_OK)

    def test_03_tail(self):
        list_ = self.linked_list_cls()
        list_.tail()
        self.assertEqual(list_.get_tail_status(), self.linked_list_cls.TAIL_EMPTY_ERR)

        list_.add_tail('1st')
        list_.add_tail('last')
        self.assertEqual(list_.get(), '1st')

        list_.tail()
        self.assertEqual(list_.get(), 'last')
        self.assertEqual(list_.get_tail_status(), self.linked_list_cls.TAIL_OK)

    def test_04_right(self):
        list_ = self.linked_list_cls()
        list_.right()
        self.assertEqual(list_.get_right_status(), self.linked_list_cls.RIGHT_EMPTY_ERR)

        list_ = self._get_filled_list('1st', 'last')

        list_.right()
        self.assertEqual(list_.get(), 'last')
        self.assertEqual(list_.get_right_status(), self.linked_list_cls.RIGHT_OK)

        list_.right()
        self.assertEqual(list_.get_right_status(), self.linked_list_cls.RIGHT_TAIL_ERR)

    def test_05_put_right(self):
        list_ = self.linked_list_cls()
        list_.put_right(0)
        self.assertEqual(list_.get_put_right_status(), self.linked_list_cls.PUT_RIGHT_EMPTY_ERR)

        list_.add_tail('1st')

        list_.put_right('last')
        self.assertEqual(list_.get_put_right_status(), self.linked_list_cls.PUT_RIGHT_OK)
        self.assertEqual(list_.get_size(), 2)
        self.assertEqual(list_.get(), '1st')

        list_.put_right('mid')
        self.assertEqual(list_.get_put_right_status(), self.linked_list_cls.PUT_RIGHT_OK)
        self.assertEqual(list_.get_size(), 3)
        self.assertEqual(list_.get(), '1st')

        list_.tail()
        self.assertEqual(list_.get(), 'last')

    def test_06_put_left(self):
        list_ = self.linked_list_cls()
        list_.put_left(0)
        self.assertEqual(list_.get_put_left_status(), self.linked_list_cls.PUT_LEFT_EMPTY_ERR)

        list_.add_tail('last')

        list_.put_left('1st')
        self.assertEqual(list_.get_put_left_status(), self.linked_list_cls.PUT_LEFT_OK)
        self.assertEqual(list_.get(), 'last')

        list_.put_left('mid')
        self.assertEqual(list_.get_put_left_status(), self.linked_list_cls.PUT_LEFT_OK)
        self.assertEqual(list_.get(), 'last')

        list_.head()
        self.assertEqual(list_.get(), '1st')

    def test_07_remove(self):
        list_ = self._get_filled_list('1st', 'mid', 'last')
        list_.right()
        self.assertEqual(list_.get(), 'mid')

        list_.remove()
        self.assertEqual(list_.get_remove_status(), self.linked_list_cls.REMOVE_OK_RIGHT)
        self.assertEqual(list_.get(), 'last')

        list_.remove()
        self.assertEqual(list_.get_remove_status(), self.linked_list_cls.REMOVE_OK_LEFT)
        self.assertEqual(list_.get(), '1st')

        list_.remove()
        self.assertEqual(list_.get_remove_status(), self.linked_list_cls.REMOVE_OK_EMPTY)

        list_.remove()
        self.assertEqual(list_.get_remove_status(), self.linked_list_cls.REMOVE_EMPTY_ERR)

    def test_08_clear(self):
        list_ = self._get_filled_list(0, 1, 2, 3,)
        list_.clear()
        self._check_initial_state(list_)

    # additional commands tests
    def test_09_add_tail(self):
        list_ = self.linked_list_cls()

        list_.add_tail('1st')
        self.assertEqual(list_.get(), '1st')
        self.assertEqual(list_.is_head(), True)
        self.assertEqual(list_.is_tail(), True)
        self.assertEqual(list_.get_size(), 1)

        list_.add_tail('last')
        self.assertEqual(list_.get(), '1st')
        self.assertEqual(list_.is_head(), True)
        self.assertEqual(list_.is_tail(), False)
        self.assertEqual(list_.get_size(), 2)

    def test_10_replace(self):
        list_ = self.linked_list_cls()
        list_.replace(0)
        self.assertEqual(list_.get_replace_status(), self.linked_list_cls.REPLACE_EMPTY_ERR)

        list_.add_tail('old_val')
        list_.replace('new_val')
        self.assertEqual(list_.get_replace_status(), self.linked_list_cls.REPLACE_OK)
        self.assertEqual(list_.get(), 'new_val')

    def test_11_find(self):
        list_ = self.linked_list_cls()
        list_.find(0)
        self.assertEqual(list_.get_find_status(), self.linked_list_cls.FIND_EMPTY)

        vals = (0, 1, 2, 0, 1, 2)
        list_ = self._get_filled_list(*vals)

        list_.find(2)
        self.assertEqual(list_.get_find_status(), self.linked_list_cls.FIND_OK)
        self.assertEqual(list_.get(), 2)
        self.assertEqual(list_.is_head(), False)
        self.assertEqual(list_.is_tail(), False)
        list_.right()
        self.assertEqual(list_.get(), 0)

        list_.find(2)
        self.assertEqual(list_.get_find_status(), self.linked_list_cls.FIND_OK)
        self.assertEqual(list_.get(), 2)
        self.assertEqual(list_.is_head(), False)
        self.assertEqual(list_.is_tail(), True)

        list_.find(2)
        self.assertEqual(list_.get_find_status(), self.linked_list_cls.FIND_NOT_FOUND)

        list_.head()
        list_.find('miss')
        self.assertEqual(list_.get_find_status(), self.linked_list_cls.FIND_NOT_FOUND)

    def test_12_remove_all(self):
        list_ = self.linked_list_cls()
        list_.remove_all(0)
        self.assertEqual(list_.get_remove_all_status(), self.linked_list_cls.REMOVE_ALL_NOTHING)

        vals = (0, 1, 2, 0, 1, 3)
        list_ = self._get_filled_list(*vals)

        list_.remove_all(0)
        self.assertEqual(list_.get_remove_all_status(), self.linked_list_cls.REMOVE_ALL_OK)
        self.assertEqual(list_.get_size(), 4)
        list_.head()
        self.assertEqual(list_.get(), 1)

        list_.remove_all(2)
        self.assertEqual(list_.get_remove_all_status(), self.linked_list_cls.REMOVE_ALL_OK)
        self.assertEqual(list_.get_size(), 3)
        list_.head()
        list_.right()
        self.assertEqual(list_.get(), 1)

        list_.remove_all(2)
        self.assertEqual(list_.get_remove_all_status(), self.linked_list_cls.REMOVE_ALL_NOTHING)
        self.assertEqual(list_.get_size(), 3)
        self.assertEqual(list_.is_tail(), True)

        vals = (0, 0, 0, 0)
        list_ = self._get_filled_list(*vals)
        list_.remove_all(0)
        self.assertEqual(list_.get_remove_all_status(), self.linked_list_cls.REMOVE_ALL_OK)
        self.assertEqual(list_.is_value(), False)
        self.assertEqual(list_.get_size(), 0)

    def test_13_get(self):
        expected_vals = list(range(5))
        list_ = self._get_filled_list(*expected_vals)

        list_.head()
        actual_vals = []
        for _ in range(list_.get_size()):
            actual_vals.append(list_.get())
            list_.right()

        self.assertEqual(actual_vals, expected_vals)

    def test_14_size(self):
        vals = tuple(range(5))
        list_ = self._get_filled_list(*vals)

        expected_size = len(vals)
        self.assertEqual(list_.get_size(), expected_size)


class LinkedListTests(__ParentListTestsMixin, unittest.TestCase):
    linked_list_cls = LinkedList


class TwoWayListTests(__ParentListTestsMixin, unittest.TestCase):
    linked_list_cls = TwoWayList

    def _check_initial_state(self, list_: linked_list_cls):
        _ = list_
        actual_params = (_.get_size(), _.is_value(),
                         _.is_head(), _.is_tail(),)
        actual_statuses = (
                _.get_find_status(), _.get_get_status(),
                _.get_head_status(), _.get_put_left_status(),
                _.get_put_right_status(), _.get_remove_all_status(),
                _.get_remove_status(), _.get_replace_status(),
                _.get_right_status(), _.get_tail_status(),
                _.get_left_status(),
            )
        actual_state = actual_params + actual_statuses

        methods_init_status = init_size = 0
        expected_state = ((init_size,) + (False,) * 3 +
                          (methods_init_status,) * len(actual_statuses))

        self.assertTupleEqual(actual_state, expected_state)

    def test_04_left(self):
        list_ = self.linked_list_cls()
        list_.left()
        self.assertEqual(list_.get_left_status(), self.linked_list_cls.LEFT_EMPTY_ERR)

        list_ = self._get_filled_list('1st', 'last')

        list_.right()
        self.assertEqual(list_.get(), 'last')
        list_.left()
        self.assertEqual(list_.get(), '1st')
        self.assertEqual(list_.get_left_status(), self.linked_list_cls.LEFT_OK)

        list_.left()
        self.assertEqual(list_.get_left_status(), self.linked_list_cls.LEFT_HEAD_ERR)


# ------------------ MAIN ----------------------

if __name__ == '__main__':
    unittest.main()

