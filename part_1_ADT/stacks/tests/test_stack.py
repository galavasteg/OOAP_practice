import unittest

from part_1_ADT.stacks import Stack


def _get_filled_stack(*vals) -> Stack:
    stack = Stack()
    for v in vals:
        stack.push(v)
    return stack


def check_size_after_push(stack: Stack, init_size: int):
    assert stack.size() == init_size + 1


def check_size_after_pop(stack: Stack, init_size: int):
    if init_size > 0:
        assert stack.size() == init_size - 1
    else:
        assert stack.size() == init_size == 0


class StackTests(unittest.TestCase):

    def test_constructor(self):
        s = Stack()
        assert isinstance(s, Stack)

    def test_clear(self):
        stack = _get_filled_stack(1, 2, 3, 4)
        stack.clear()
        assert stack.size() == 0
        assert stack.get_peek_status() == stack.PEEK_NIL
        assert stack.get_pop_status() == stack.POP_NIL

    def test_size(self):
        stack = Stack()
        assert stack.size() == 0

        for vals, init_size in zip(
                (tuple('(()()(()'), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), ),
                (8, 10, )):
            stack = _get_filled_stack(*vals)
            assert stack.size() == init_size
            stack.push(None)
            check_size_after_push(stack, init_size)
            stack.pop()
            assert stack.size() == init_size

    def test_push(self):
        for vals, adds in zip(
                (((1, 2), (3, 4)), ((), (0,)),
                 (list(range(5)), list(range(5, 0, -1)))),
                ([1, 2, 3, 4], [], [0], [None], [0,1,2,3,4,5,4,3,2,1])):
            stack = _get_filled_stack(*vals)

            size = stack.size()
            for a in adds:
                stack.push(a)
                check_size_after_push(stack, size)

                size = stack.size()

    def test_pop(self):
        stack = Stack()

        assert stack.get_pop_status() == stack.POP_NIL

        stack.pop()
        assert stack.get_pop_status() == stack.POP_ERR

        for vals in ((1, 2, 3, 4),
                     (0,),
                     (None, 0, 17)):
            stack = _get_filled_stack(*vals)
            init_size = stack.size()
            stack.pop()

            assert stack.get_pop_status() == stack.POP_OK
            check_size_after_pop(stack, init_size)

    def test_peek(self):
        stack = Stack()

        assert stack.get_peek_status() == stack.PEEK_NIL

        _ = stack.peek()
        assert stack.get_peek_status() == stack.PEEK_ERR

        for vals, correct_p in (((1, 2, 3, 4), 4),
                                ((0,), 0),
                                ((None, 0, 17), 17)):
            stack = _get_filled_stack(*vals)
            p = stack.peek()

            assert p == correct_p
            assert stack.get_peek_status() == stack.PEEK_OK

    def test_fill_and_empty(self):
        stack = Stack()
        n = 10000
        for v in range(n):
            stack.push(v)
        assert stack.size() == n

        for _ in range(n):
            stack.pop()
        assert stack.size() == 0
        assert stack.get_pop_status() == stack.POP_OK


# ------------------ MAIN ----------------------

if __name__ == '__main__':
    unittest.main()

