from random import choice
import unittest

from dynamic_array import DynamicArray
from .test_dynamic_array import (
        DynamicArrayTestsBase,
        EmptyTests,
        PartialFilledTests,
    )


class EmptyTests(DynamicArrayTestsBase, EmptyTests):

    def test_04_empty_getitem_bad_slice_type(self):
        _ = self.dyn_array[:'5':]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_TYPE_ERR)

    def test_05_empty_getitem_bad_slice_1(self):
        _ = self.dyn_array[:]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_05_empty_getitem_bad_slice_2(self):
        _ = self.dyn_array[-1:]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_05_empty_getitem_bad_slice_3(self):
        _ = self.dyn_array[:2]

        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OUT_OF_BOUNDS_ERR)


class PartialFilledTests(DynamicArrayTestsBase, PartialFilledTests):

    def test_11_partial_getitem_bad_slice_1(self):
        items = self.dyn_array[:9]

        self.assertEqual(items, ())
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_11_partial_getitem_bad_slice_2(self):
        items = self.dyn_array[-10:-2]

        self.assertEqual(items, ())
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OUT_OF_BOUNDS_ERR)

    def test_13_partial_getitem_slice_1(self):
        items = self.dyn_array[1:5]

        expected_items = tuple(self.init_items[1:5])
        self.assertEqual(items, expected_items)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OK)

    def test_13_partial_getitem_slice_2(self):
        items = self.dyn_array[-7:-2]

        expected_items = tuple(self.init_items[-7:-2])
        self.assertEqual(items, expected_items)
        self.assertEqual(self.dyn_array.get_getitem_status(),
                         DynamicArray.GETITEM_OK)


if __name__ == '__main__':
    unittest.main()

