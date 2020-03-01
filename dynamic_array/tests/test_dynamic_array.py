from collections.abc import Iterable
from random import choice
import unittest

from dynamic_array import DynamicArray


class DynamicArrayTestsBase(unittest.TestCase):

    ARRAY_CLS = DynamicArray
    INIT_ITEMS = range(0)

    def setUp(self):
        self.dyn_array = self.ARRAY_CLS()
        self.dyn_array = self.get_filled_array(self.INIT_ITEMS)

    @classmethod
    def get_filled_array(cls, vals: Iterable) -> ARRAY_CLS:
        da = cls.ARRAY_CLS()
        for v in vals:
            da.append(v)
        return da

    @staticmethod
    def get_array_items(array: ARRAY_CLS):
        items = tuple(map(lambda i: array[i], range(len(array))))
        return items

    def check_items_after_ins(self, array: ARRAY_CLS,
                              ins_index: int = None, ins_item: object = None):
        actual_items = self.get_array_items(array)
        if ins_index is not None:
            expected_items = (tuple(self.INIT_ITEMS[:ins_index]) + (ins_item,) +
                              tuple(self.INIT_ITEMS[ins_index:]))
        else:
            expected_items = tuple(self.INIT_ITEMS)

        self.assertEqual(array[ins_index], ins_item)
        self.assertTupleEqual(actual_items, expected_items)

    def check_items_after_del(self, array: ARRAY_CLS, del_index: int = None):
        actual_items = self.get_array_items(array)
        if del_index is not None:
            expected_items = (tuple(self.INIT_ITEMS[:del_index]) +
                              tuple(self.INIT_ITEMS[del_index + 1:]))
        else:
            expected_items = tuple(self.INIT_ITEMS)

        self.assertTupleEqual(actual_items, expected_items)

    def check_meta_after_insert(self, array: ARRAY_CLS,
                                expected_size: int, expected_capacity: int,
                                expected_ins_status: int):
        # TODO: split on two functions
        self.assertEqual(len(array), expected_size)
        self.assertEqual(array.get_capacity(), expected_capacity)
        self.assertEqual(array.get_insert_status(), expected_ins_status)

    def check_meta_after_delete(self, array: ARRAY_CLS,
                                expected_size: int, expected_capacity: int,
                                expected_del_status: int):
        self.assertEqual(len(array), expected_size)
        self.assertEqual(array.get_capacity(), expected_capacity)
        self.assertEqual(array.get_delete_status(), expected_del_status)


class DA1EmptyTests(DynamicArrayTestsBase):

    INIT_ITEMS = range(0)

    def test_01_constructor(self):
        _ = self.dyn_array
        actual_params = (len(_), _.get_capacity(),)
        actual_statuses = (
            _.get_getitem_status(),
            _.get_insert_status(),
            _.get_delete_status(),
        )
        actual_state = actual_params + actual_statuses

        methods_init_status = init_size = 0
        expected_state = ((init_size, self.ARRAY_CLS.INITIAL_CAPACITY) +
                          (methods_init_status,) * len(actual_statuses))

        self.assertTupleEqual(actual_state, expected_state)

    def test_02_empty_getitem_bad_ind_type(self):
        _ = self.dyn_array['wrong index']

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_TYPE_ERR)

    def test_03_empty_getitem_bad_ind_1(self):
        _ = self.dyn_array[0]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_03_empty_getitem_bad_ind_2(self):
        _ = self.dyn_array[5]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_03_empty_getitem_bad_ind_3(self):
        _ = self.dyn_array[-1]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_04_empty_insert_bad_ind_type(self):
        self.dyn_array.insert('', 'item')

        self.check_items_after_ins(self.dyn_array)
        self.check_meta_after_insert(self.dyn_array, 0,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_TYPE_ERR)

    def test_05_empty_insert_bad_ind(self):
        self.dyn_array.insert(6, 'item')

        self.check_items_after_ins(self.dyn_array)
        self.check_meta_after_insert(self.dyn_array, 0,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_06_empty_insert_head(self):
        self.dyn_array.insert(0, 'item')

        self.check_items_after_ins(self.dyn_array, 0, 'item')
        self.check_meta_after_insert(self.dyn_array, 1,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_07_empty_append(self):
        self.dyn_array.append('item')

        self.check_items_after_ins(self.dyn_array, 0, 'item')
        self.check_meta_after_insert(self.dyn_array, 1,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_08_empty_delete_bad_ind_type(self):
        self.dyn_array.delete('wrong index')

        self.check_items_after_del(self.dyn_array)
        self.check_meta_after_delete(self.dyn_array, 0,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_TYPE_ERR)

    def test_09_empty_delete_bad_ind_1(self):
        self.dyn_array.delete(0)

        self.check_items_after_del(self.dyn_array)
        self.check_meta_after_delete(self.dyn_array, 0,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_09_empty_delete_bad_ind_2(self):
        self.dyn_array.delete(-1)

        self.check_items_after_del(self.dyn_array)
        self.check_meta_after_delete(self.dyn_array, 0,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)


class DA2PartialFilledTests(DynamicArrayTestsBase):

    INIT_ITEMS = range(8)

    def test_01_partial_getitem_bad_ind_1(self):
        _ = self.dyn_array[8]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_01_partial_getitem_bad_ind_2(self):
        _ = self.dyn_array[-9]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_02_partial_getitem_ind_1(self):
        five = self.dyn_array[5]

        self.assertEqual(five, 5)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_02_partial_getitem_ind_2(self):
        four = self.dyn_array[-4]

        self.assertEqual(four, 4)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_03_partial_insert_bad_ind_1(self):
        self.dyn_array.insert(10, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_03_partial_insert_bad_ind_2(self):
        self.dyn_array.insert(-12, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_04_partial_insert_ind_1(self):
        self.dyn_array.insert(4, 'item')

        self.check_items_after_ins(self.dyn_array, 4, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_04_partial_insert_ind_2(self):
        self.dyn_array.insert(8, 'item')

        self.check_items_after_ins(self.dyn_array, 8, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_04_partial_insert_ind_3(self):
        self.dyn_array.insert(-1, 'item')  # 8 elements, -1 <==> 7

        self.check_items_after_ins(self.dyn_array, 7, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_05_partial_append(self):
        self.dyn_array.append('item')

        ins_index = len(self.INIT_ITEMS)
        self.check_items_after_ins(self.dyn_array, ins_index, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_06_partial_delete_bad_ind_1(self):
        self.dyn_array.delete(8)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_06_partial_delete_bad_ind_2(self):
        self.dyn_array.delete(-9)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_07_partial_delete_ind_1(self):
        self.dyn_array.delete(4)

        self.check_items_after_del(self.dyn_array, 4)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_07_partial_delete_ind_2(self):
        self.dyn_array.delete(-1)  # 8 items, -1 <==> 7

        self.check_items_after_del(self.dyn_array, 7)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_08_partial_delete_many(self):
        for _ in range(3):
            self.dyn_array.delete(0)

        expected_items = tuple(self.INIT_ITEMS[3:])
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = len(expected_items)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)


class DA3IncreaseCapacityTests(DynamicArrayTestsBase):

    INIT_ITEMS = range(16)

    def test_00_full_getitem_bad_ind_1(self):
        _ = self.dyn_array[17]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_00_full_getitem_bad_ind_2(self):
        _ = self.dyn_array[-20]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_01_full_getitem_ind_1(self):
        nine = self.dyn_array[9]

        self.assertEqual(nine, 9)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_01_full_getitem_ind_2(self):
        seven = self.dyn_array[-9]

        self.assertEqual(seven, 7)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_01_full_getitem_ind_3(self):
        fifteen = self.dyn_array[-1]

        self.assertEqual(fifteen, 15)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_02_full_insert_bad_ind_1(self):
        self.dyn_array.insert(17, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_02_full_insert_bad_ind_2(self):
        self.dyn_array.insert(-20, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_03_full_insert_ind_1(self):
        self.dyn_array.insert(0, 'item')

        self.check_items_after_ins(self.dyn_array, 0, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY * 2,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_03_full_insert_ind_2(self):
        self.dyn_array.insert(8, 'item')

        self.check_items_after_ins(self.dyn_array, 8, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY * 2,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_03_full_insert_ind_3(self):
        self.dyn_array.insert(-1, 'item')  # 16 elements, -1 <==> 15

        self.check_items_after_ins(self.dyn_array, 15, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY * 2,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_04_full_append(self):
        self.dyn_array.append('item')

        ins_index = len(self.INIT_ITEMS)
        self.check_items_after_ins(self.dyn_array, ins_index, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY * 2,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_05_full_delete_bad_ind_1(self):
        self.dyn_array.delete(16)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_05_full_delete_bad_ind_2(self):
        self.dyn_array.delete(-19)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_06_full_delete_ind_1(self):
        self.dyn_array.delete(4)

        self.check_items_after_del(self.dyn_array, 4)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_06_full_delete_ind_2(self):
        self.dyn_array.delete(-1)  # 16 items, -1 <==> 15

        self.check_items_after_del(self.dyn_array, 15)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_06_full_delete_many(self):
        for _ in range(9):
            self.dyn_array.delete(0)

        expected_items = tuple(self.INIT_ITEMS[9:])
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = len(expected_items)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.ARRAY_CLS.INITIAL_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)


class DA4DecreaseCapacityTests(DynamicArrayTestsBase):

    INIT_ITEMS = range(65)
    INIT_CAPACITY = 128

    def test_00_big_capacity_getitem_bad_ind_1(self):
        _ = self.dyn_array[65]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_00_big_capacity_getitem_bad_ind_2(self):
        _ = self.dyn_array[-70]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_01_big_capacity_getitem_ind_1(self):
        nine = self.dyn_array[9]

        self.assertEqual(nine, 9)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_01_big_capacity_getitem_ind_2(self):
        fifty_six = self.dyn_array[-9]  # 65 items, -9 <==> 56

        self.assertEqual(fifty_six, 56)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_01_big_capacity_getitem_ind_3(self):
        sixty_four = self.dyn_array[-1]

        self.assertEqual(sixty_four, 64)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_02_big_capacity_insert_bad_ind_1(self):
        self.dyn_array.insert(66, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_02_big_capacity_insert_bad_ind_2(self):
        self.dyn_array.insert(-70, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_03_big_capacity_insert_ind_1(self):
        self.dyn_array.insert(0, 'item')

        self.check_items_after_ins(self.dyn_array, 0, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_03_big_capacity_insert_ind_2(self):
        self.dyn_array.insert(32, 'item')

        self.check_items_after_ins(self.dyn_array, 32, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_03_big_capacity_insert_ind_3(self):
        self.dyn_array.insert(-1, 'item')  # 65 elements, -1 <==> 64

        self.check_items_after_ins(self.dyn_array, 64, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_04_big_capacity_append(self):
        self.dyn_array.append('item')

        ins_index = len(self.INIT_ITEMS)
        self.check_items_after_ins(self.dyn_array, ins_index, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_05_big_capacity_delete_bad_ind_1(self):
        self.dyn_array.delete(65)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_05_big_capacity_delete_bad_ind_2(self):
        self.dyn_array.delete(-70)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_06_big_capacity_delete_ind_1(self):
        self.dyn_array.delete(4)

        self.check_items_after_del(self.dyn_array, 4)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_06_big_capacity_delete_ind_2(self):
        self.dyn_array.delete(-1)  # 65 items, -1 <==> 64

        self.check_items_after_del(self.dyn_array, 64)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_07_big_capacity_delete_many_1(self):
        for _ in range(9):
            self.dyn_array.delete(0)

        expected_items = tuple(self.INIT_ITEMS[9:])
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = len(expected_items)
        expected_capacity = int(self.INIT_CAPACITY / 1.5)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     expected_capacity,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_07_big_capacity_delete_many_2(self):
        for _ in range(37):
            self.dyn_array.delete(0)

        expected_items = tuple(self.INIT_ITEMS[37:])
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = len(expected_items)
        expected_capacity = int(int(self.INIT_CAPACITY / 1.5) / 1.5)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     expected_capacity,
                                     self.ARRAY_CLS.DELETE_OK)


class DA4DecreaseCapacityTests(DynamicArrayTestsBase):

    INIT_ITEMS = range(65)
    INIT_CAPACITY = 128

    def test_00_big_capacity_getitem_bad_ind_1(self):
        _ = self.dyn_array[65]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_00_big_capacity_getitem_bad_ind_2(self):
        _ = self.dyn_array[-70]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_01_big_capacity_getitem_ind_1(self):
        nine = self.dyn_array[9]

        self.assertEqual(nine, 9)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_01_big_capacity_getitem_ind_2(self):
        fifty_six = self.dyn_array[-9]  # 65 items, -9 <==> 56

        self.assertEqual(fifty_six, 56)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_01_big_capacity_getitem_ind_3(self):
        sixty_four = self.dyn_array[-1]

        self.assertEqual(sixty_four, 64)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         self.ARRAY_CLS.GETITEM_OK)

    def test_02_big_capacity_insert_bad_ind_1(self):
        self.dyn_array.insert(66, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_02_big_capacity_insert_bad_ind_2(self):
        self.dyn_array.insert(-70, 'item')

        self.check_items_after_ins(self.dyn_array)

        init_size = len(self.INIT_ITEMS)
        self.check_meta_after_insert(self.dyn_array, init_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_BOUNDS_ERR)

    def test_03_big_capacity_insert_ind_1(self):
        self.dyn_array.insert(0, 'item')

        self.check_items_after_ins(self.dyn_array, 0, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_03_big_capacity_insert_ind_2(self):
        self.dyn_array.insert(32, 'item')

        self.check_items_after_ins(self.dyn_array, 32, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_03_big_capacity_insert_ind_3(self):
        self.dyn_array.insert(-1, 'item')  # 65 elements, -1 <==> 64

        self.check_items_after_ins(self.dyn_array, 64, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_04_big_capacity_append(self):
        self.dyn_array.append('item')

        ins_index = len(self.INIT_ITEMS)
        self.check_items_after_ins(self.dyn_array, ins_index, 'item')

        expected_size = len(self.INIT_ITEMS) + 1
        self.check_meta_after_insert(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.INSERT_OK)

    def test_05_big_capacity_delete_bad_ind_1(self):
        self.dyn_array.delete(65)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_05_big_capacity_delete_bad_ind_2(self):
        self.dyn_array.delete(-70)

        self.check_items_after_del(self.dyn_array)
        expected_size = len(self.INIT_ITEMS)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_BOUNDS_ERR)

    def test_06_big_capacity_delete_ind_1(self):
        self.dyn_array.delete(4)

        self.check_items_after_del(self.dyn_array, 4)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_06_big_capacity_delete_ind_2(self):
        self.dyn_array.delete(-1)  # 65 items, -1 <==> 64

        self.check_items_after_del(self.dyn_array, 64)
        expected_size = len(self.INIT_ITEMS) - 1
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     self.INIT_CAPACITY,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_07_big_capacity_delete_many_1(self):
        for _ in range(9):
            self.dyn_array.delete(0)

        expected_items = tuple(self.INIT_ITEMS[9:])
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = len(expected_items)
        expected_capacity = int(self.INIT_CAPACITY / 1.5)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     expected_capacity,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_07_big_capacity_delete_many_2(self):
        for _ in range(37):
            self.dyn_array.delete(0)

        expected_items = tuple(self.INIT_ITEMS[37:])
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = len(expected_items)
        expected_capacity = int(int(self.INIT_CAPACITY / 1.5) / 1.5)
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     expected_capacity,
                                     self.ARRAY_CLS.DELETE_OK)


class DA5FillDeleteTests(DynamicArrayTestsBase):

    INIT_ITEMS = range(1023)
    INIT_CAPACITY = 1024

    def test_01_delete_all(self):
        for _ in range(len(self.INIT_ITEMS)):
            self.dyn_array.delete(0)

        expected_items = ()
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = 0
        expected_capacity = self.ARRAY_CLS.INITIAL_CAPACITY
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     expected_capacity,
                                     self.ARRAY_CLS.DELETE_OK)

    def test_01_delete_all_randomly(self):
        for _ in range(len(self.INIT_ITEMS)):
            del_i = choice(range(len(self.dyn_array)))
            self.dyn_array.delete(del_i)

        expected_items = ()
        actual_items = self.get_array_items(self.dyn_array)
        self.assertTupleEqual(actual_items, expected_items)

        expected_size = 0
        expected_capacity = self.ARRAY_CLS.INITIAL_CAPACITY
        self.check_meta_after_delete(self.dyn_array, expected_size,
                                     expected_capacity,
                                     self.ARRAY_CLS.DELETE_OK)

if __name__ == '__main__':
    unittest.main()

