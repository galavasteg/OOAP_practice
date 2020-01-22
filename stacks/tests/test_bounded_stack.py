import unittest

from stacks.bounded_stack import BoundedStack as BStack


def _get_filled_stack(*vals) -> BStack:
    stack = BStack()
    for v in vals:
        stack.push(v)
    return stack


class StackTests(unittest.TestCase):

    def _check_size_after_push(self, stack: BStack, init_size: int):
        if init_size < stack.get_max_size():
            expected_size = init_size + 1
        else:
            expected_size = stack.get_max_size()
        self.assertEqual(stack.size, expected_size)

    def _check_size_after_pop(self, stack: BStack, init_size: int):
        if init_size > 0:
            expected_size = init_size - 1
        else:
            expected_size = init_size
        self.assertEqual(stack.size, expected_size)

    def test_constructor(self):
        self.assertRaises(TypeError, BStack, 'fail')
        self.assertRaises(TypeError, BStack, '4.5')
        self.assertRaises(TypeError, BStack, [1])
        self.assertRaises(TypeError, BStack, '5')
        self.assertRaises(ValueError, BStack, -10)
        self.assertRaises(ValueError, BStack, 0)

        s = BStack()
        to_check_params = (s.get_max_size(), s.get_peek_status(),
                           s.get_pop_status(), s.get_push_status(),)
        expected_state = (BStack.get_def_max_size(), BStack.PEEK_NIL,
                          BStack.POP_NIL, BStack.PUSH_NIL,)
        self.assertTupleEqual(to_check_params, expected_state)

        new_max_size = 4
        stack = BStack(new_max_size)
        self.assertEqual(stack.get_max_size(), new_max_size)

        new_def_max_size = 15
        BStack.set_def_max_size(new_def_max_size)
        stack = BStack()
        self.assertEqual(stack.get_max_size(), new_def_max_size)

    def test_clear(self):
        s = _get_filled_stack(1, 2, 3, 4)
        s.clear()
        to_check_params = (s.size, s.get_peek_status(),
                           s.get_pop_status(), s.get_push_status(),)
        expected_state = (0, BStack.PEEK_NIL,
                          BStack.POP_NIL, BStack.PUSH_NIL,)
        self.assertTupleEqual(to_check_params, expected_state)

        s = _get_filled_stack(1, 2, 3, 4)
        # reset default class-property
        old_def_max_size = BStack.get_def_max_size()
        new_def_max_size = 15
        BStack.set_def_max_size(new_def_max_size)
        s.clear()
        self.assertEqual(s.get_max_size(), old_def_max_size)

    def test_size(self):
        stack = BStack()
        self.assertEqual(stack.size, 0)

        vals = (1, 2, 3, 4, 5,)
        stack = _get_filled_stack(*vals)
        expected_size = len(vals)
        self.assertEqual(stack.size, expected_size)

    def test_push(self):
        stack = BStack(1)
        self.assertEqual(stack.get_push_status(), BStack.PUSH_NIL)

        init_size = 0
        stack.push(1)
        self._check_size_after_push(stack, init_size)
        self.assertEqual(stack.get_push_status(), BStack.PUSH_OK)

        init_size = 1
        stack.push(2)
        self._check_size_after_push(stack, init_size)
        self.assertEqual(stack.get_push_status(), BStack.PUSH_ERR)

    def test_pop(self):
        stack = BStack(1)
        self.assertEqual(stack.get_pop_status(), BStack.POP_NIL)

        stack.push(1)
        init_size = 1
        stack.pop()
        self._check_size_after_pop(stack, init_size)
        self.assertEqual(stack.get_pop_status(), BStack.POP_OK)

        init_size = 0
        stack.pop()
        self._check_size_after_pop(stack, init_size)
        self.assertEqual(stack.get_pop_status(), BStack.POP_ERR)

    def test_peek(self):
        stack = BStack(2)
        self.assertEqual(stack.get_peek_status(), BStack.PEEK_NIL)
        _ = stack.peek()
        self.assertEqual(stack.get_peek_status(), BStack.PEEK_ERR)

        expected_val = 1
        stack.push(expected_val)
        val = stack.peek()
        self.assertEqual(val, expected_val)
        self.assertEqual(stack.get_peek_status(), BStack.PEEK_OK)

        expected_val = 2
        stack.push(expected_val)
        val = stack.peek()
        self.assertEqual(val, expected_val)
        self.assertEqual(stack.get_peek_status(), BStack.PEEK_OK)

        stack.pop()
        stack.pop()
        _ = stack.peek()
        self.assertEqual(stack.get_peek_status(), BStack.PEEK_ERR)

    def test_fill_and_empty(self):
        big_stack = BStack(10000)
        n = 10001
        for v in range(n):
            big_stack.push(v)
        self.assertEqual(big_stack.get_push_status(), BStack.PUSH_ERR)
        self.assertEqual(big_stack.size, big_stack.get_max_size())

        for _ in range(n):
            big_stack.pop()
        self.assertEqual(big_stack.get_pop_status(), BStack.PUSH_ERR)
        self.assertEqual(big_stack.size, 0)


# ------------------ MAIN ----------------------

if __name__ == '__main__':
    unittest.main()

