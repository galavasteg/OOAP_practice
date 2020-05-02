import unittest

from native_dictionary import Dictionary


class DictTestsBase(unittest.TestCase):

    INIT_ITEMS = None

    def setUp(self):
        if self.INIT_ITEMS is None:
            raise AttributeError('Set INIT_ITEMS')

        d = Dictionary()

        for k, v in self.INIT_ITEMS:
            d[k] = v

        self.dict = d


class D1EmptyTests(DictTestsBase):

    INIT_ITEMS = ()

    def test_01_constructor(self):
        d = self.dict

        actual_params = (len(d), )
        expected_params = (len(self.INIT_ITEMS), )
        self.assertTupleEqual(actual_params, expected_params)

        actual_statuses = (
                d.get_getitem_status(),
                d.get_remove_status(),
            )
        expected_statuses = (
                Dictionary.GETITEM_NIL,
                Dictionary.REMOVE_NIL,
            )
        self.assertTupleEqual(actual_statuses, expected_statuses)

    def test_02_empty_getitem_bad(self):
        _ = self.dict['item']

        self.assertEqual(self.dict.get_getitem_status(),
                         Dictionary.GETITEM_KEY_ERR)

    def test_03_empty_setitem(self):
        self.dict['item'] = 13

        self.assertEqual(self.dict['item'], 13)
        self.assertEqual(len(self.dict), 1)

    def test_04_empty_remove_bad(self):
        self.dict.remove('item')

        self.assertEqual(self.dict.get_remove_status(),
                         Dictionary.REMOVE_KEY_ERR)

    def test_05_empty_iskey(self):
        self.assertFalse(self.dict.is_key('item'))


class D2FilledTests(DictTestsBase):

    INIT_ITEMS = (('0', 0), ('4', 4), )

    def test_01_filled_getitem_ok(self):
        four = self.dict['4']

        self.assertEqual(four, 4)
        self.assertEqual(self.dict.get_getitem_status(),
                         Dictionary.GETITEM_OK)

    def test_02_filled_setitem_update(self):
        self.dict['4'] = 44

        self.assertEqual(self.dict['4'], 44)
        self.assertEqual(len(self.dict),
                         len(self.INIT_ITEMS))

    def test_03_filled_setitem_collision(self):
        self.dict['5'] = 5

        self.assertEqual(self.dict['5'], 5)
        self.assertEqual(len(self.dict),
                         len(self.INIT_ITEMS) + 1)
        self.assertEqual(self.dict._busy_slots_count,
                         len(self.INIT_ITEMS))

    def test_04_filled_remove_ok(self):
        self.dict.remove('4')

        self.assertFalse(self.dict.is_key('4'))
        self.assertEqual(len(self.dict),
                         len(self.INIT_ITEMS) - 1)
        self.assertEqual(self.dict._busy_slots_count,
                         len(self.INIT_ITEMS) - 1)
        self.assertEqual(self.dict.get_remove_status(),
                         Dictionary.REMOVE_OK)

    def test_05_filled_iskey(self):
        self.assertTrue(self.dict.is_key('4'))

    def test_06_filled_keys_method(self):
        expected_keys = set(map(lambda k_v: k_v[0],
                                self.INIT_ITEMS))

        keys = set(self.dict.keys())
        self.assertEqual(keys, expected_keys)

        keys = set(self.dict)
        self.assertEqual(keys, expected_keys)

    def test_07_filled_items(self):
        items = set(self.dict.items())
        self.assertEqual(items, set(self.INIT_ITEMS))


class D3ExpandTests(DictTestsBase):

    INIT_ITEMS = (
        ('40', 40), ('17', 17), ('47', 47), ('11', 11),
        ('41', 41), ('18', 18), ('48', 48), ('12', 12),
        ('0', 0), ('19', 19), ('49', 49), ('13', 13),
        ('43', 43), ('22', 22), ('2', 2),
    )
    INIT_CAPACITY = 16

    def test_01_setitem_expand(self):
        expected_capacity = (
                self.INIT_CAPACITY * Dictionary.CAPACITY_MULTIPLIER)

        self.dict['10'] = 10

        self.assertEqual(self.dict._capacity, expected_capacity)


class D3ShrinkTests(DictTestsBase):

    INIT_ITEMS = (
        ('40', 40), ('17', 17), ('47', 47), ('11', 11),
        ('41', 41), ('18', 18), ('48', 48), ('12', 12),
        ('0', 0), ('19', 19), ('49', 49), ('13', 13),
        ('43', 43), ('22', 22), ('2', 2), ('10', 10)
    )
    INIT_CAPACITY = 32

    def test_01_remove_shrink(self):
        expected_capacity = int(
                self.INIT_CAPACITY / Dictionary.CAPACITY_DELIMITER)

        self.dict.remove('40')

        self.assertEqual(self.dict._capacity, expected_capacity)

    def test_02_remove_shrink_to_min_capacity(self):

        for _, key in zip(range(6), self.dict.keys()):
            self.dict.remove(key)

        self.assertEqual(self.dict._capacity,
                         Dictionary.MIN_CAPACITY)


class D5RemoveAllTests(DictTestsBase):

    DICT_SIZE = 10000
    INIT_ITEMS = tuple(zip(map(str, range(DICT_SIZE)),
                           range(DICT_SIZE)))

    def test_01_remove_all(self):
        for key in self.dict:
            self.dict.remove(key)

        self.assertEqual(len(self.dict), 0)


if __name__ == '__main__':
    unittest.main()
