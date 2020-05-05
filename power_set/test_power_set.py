import unittest

from power_set import PowerSet


class PowerSetTestsBase(unittest.TestCase):

    INIT_ITEMS = None

    def setUp(self):
        if self.INIT_ITEMS is None:
            raise AttributeError('Set INIT_ITEMS')

        s = PowerSet()

        for v in self.INIT_ITEMS:
            s.put(v)

        self.set = s


class PowerSet1EmptyTests(PowerSetTestsBase):

    INIT_ITEMS = ()


if __name__ == '__main__':
    unittest.main()
