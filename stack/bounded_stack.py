from .abstract_data_types.abstract_bounded_stack import AbstractBoundedStack


class BoundedStack(AbstractBoundedStack):

    # class interface that implements AbstractBoundedStack
    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct value
    PEEK_ERR = 2  # stack storage is empty

    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PUSH_NIL = 0  # push() not called yet
    PUSH_OK = 1   # last push() call returned correct value
    PUSH_ERR = 2  # stack storage is full

    __DEFAULT_MAX_SIZE = 32


