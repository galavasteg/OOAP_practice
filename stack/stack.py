from .abstract_data_types.abstract_stack import AbstractStack


class Stack(AbstractStack):

    # class interface that implements AbstractStack
    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct value
    PEEK_ERR = 2  # stack storage is empty

