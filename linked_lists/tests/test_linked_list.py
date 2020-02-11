import unittest

from linked_lists.lists import LinkedList, TwoWayList


class __ParentListTestsMixin:
    linked_list_cls = None

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


# ------------------ MAIN ----------------------

if __name__ == '__main__':
    unittest.main()

