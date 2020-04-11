import unittest

from hash_table import HashTable


class HTTestsBase(unittest.TestCase):

    HT_SIZE = None
    INIT_ITEMS = None

    def setUp(self):
        if not all(map(None.__ne__, (self.HT_SIZE, self.INIT_ITEMS))):
            raise AttributeError('Set attributes: HT_SIZE, INIT_ITEMS')

        ht = HashTable(self.HT_SIZE)

        for v in self.INIT_ITEMS:
            ht.put(v)

        self.ht = ht


class HT1EmptyTests(HTTestsBase):

    HT_SIZE = 10
    INIT_ITEMS = ()

    def test_01_constructor(self):
        _ = self.ht

        actual_params = (len(_), _.get_capacity(), )
        expected_params = (len(self.INIT_ITEMS), self.HT_SIZE,)
        self.assertTupleEqual(actual_params, expected_params)

        actual_statuses = (
                _.get_put_status(),
                _.get_remove_status(),
            )
        expected_statuses = (
                HashTable.PUT_NIL,
                HashTable.REMOVE_NIL,
            )
        self.assertTupleEqual(actual_statuses, expected_statuses)

    def test_02_empty_put(self):
        self.ht.put('item')

        self.assertTrue(self.ht.is_value('item'))
        self.assertEqual(self.ht.get_put_status(),
                         HashTable.PUT_OK)

    def test_03_empty_remove_bad(self):
        self.ht.remove('item')

        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_NOVALUE_ERR)

    def test_04_empty_isvalue(self):
        self.assertFalse(self.ht.is_value('item'))


class HT2PartialFilledTests(HTTestsBase):

    HT_SIZE = 10
    INIT_ITEMS = ('ab', 'rf', 'eg', 'item')

    def test_01_partial_filled_put_ok(self):
        self.ht.put('val')

        self.assertTrue(self.ht.is_value('val'))
        self.assertEqual(self.ht.get_put_status(),
                         HashTable.PUT_OK)

    def test_02_partial_filled_put_ok_collision(self):
        self.ht.put('r')

        self.assertTrue(self.ht.is_value('r'))
        self.assertEqual(self.ht.get_put_status(),
                         HashTable.PUT_OK)

    def test_03_partial_filled_put_bad_exists(self):
        self.ht.put('ab')

        self.assertTrue(self.ht.is_value('ab'))
        self.assertEqual(self.ht.get_put_status(),
                         HashTable.PUT_EXISTS_ERR)

    def test_04_partial_filled_put_bad_collision(self):
        self.ht.put('ba')

        self.assertFalse(self.ht.is_value('ba'))
        self.assertEqual(self.ht.get_put_status(),
                         HashTable.PUT_COLLISION_ERR)

    def test_05_partial_filled_remove_ok(self):
        self.ht.remove('ab')

        self.assertFalse(self.ht.is_value('ab'))
        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_OK)

    def test_06_partial_filled_remove_bad(self):
        self.ht.remove('val')

        self.assertFalse(self.ht.is_value('val'))
        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_NOVALUE_ERR)

    def test_07_partial_filled_remove_bad_rm_collision(self):
        self.ht.remove('ba')

        self.assertTrue(self.ht.is_value('ab'))
        self.assertFalse(self.ht.is_value('ba'))
        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_NOVALUE_ERR)


class HT3FilledTests(HTTestsBase):

    HT_SIZE = 10
    INIT_ITEMS = tuple(map(str, range(HT_SIZE)))

    def test_01_filled_put_bad_filled(self):
        self.ht.put('val')

        self.assertFalse(self.ht.is_value('val'))
        self.assertEqual(self.ht.get_put_status(),
                         HashTable.PUT_FULL_ERR)

    def test_02_partial_filled_remove_ok(self):
        self.ht.remove('1')

        self.assertFalse(self.ht.is_value('1'))
        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_OK)

    def test_03_partial_filled_remove_bad(self):
        self.ht.remove('val')

        self.assertFalse(self.ht.is_value('val'))
        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_NOVALUE_ERR)

    def test_04_partial_filled_remove_bad_rm_collision(self):
        self.ht.remove('n')

        self.assertTrue(self.ht.is_value('2'))
        self.assertFalse(self.ht.is_value('n'))
        self.assertEqual(self.ht.get_remove_status(),
                         HashTable.REMOVE_NOVALUE_ERR)


class HT4CollisionTests(HTTestsBase):

    HT_SIZE = 10
    INIT_ITEMS = ('2', '3', '4',
                  'n', '6', '7',
                  'x', '9', '0',
                  '5',)
                 # ^collisions

    def setUp(self):
        HashTable.STEP = 3
        super().setUp()

    def test_01_remove_collision_with_rebalance(self):
        print(tuple(self.ht._values))
        self.ht.remove('2')

        actual_values = tuple(self.ht._values)
        expected_values = ('x', '3', '4',
                           'n', '6', '7',
                           '5', '9', '0',
                           None,)
                          # ^ collisions offset

        self.assertTupleEqual(actual_values, expected_values)


class HT5RemoveAllTests(HTTestsBase):

    HT_SIZE = 1000
    INIT_ITEMS = tuple(map(str, range(HT_SIZE)))

    def test_01_remove_all(self):
        for v in self.INIT_ITEMS:
            self.ht.remove(v)

        self.assertEqual(len(self.ht), 0)


if __name__ == '__main__':
    unittest.main()
