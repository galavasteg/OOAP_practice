from .abstract_data_types.abstract_stack import AbstractStack


class Stack(AbstractStack):

    # class interface that implements AbstractStack
    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct value
    PEEK_ERR = 2  # stack storage is empty

    def __init__(self):
        super().__init__()

        # private attributes
        self.__stack = None  # main stack storage
        self.__peek_status = None  # last peek() call status
        self.__pop_status = None  # last pop() call status

        self.clear()

    def clear(self):
        self.__stack = []  # empty list

        # initial statuses for peek() and pop() pre-conditions
        self.__peek_status = self.PEEK_NIL
        self.__pop_status = self.POP_NIL

