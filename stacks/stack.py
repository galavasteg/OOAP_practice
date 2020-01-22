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

        # private attributes:

        # main stack storage
        self.__stack = []  # empty list as stack storage

        # initial statuses for peek() and pop() pre-conditions
        self.__peek_status = self.PEEK_NIL
        self.__pop_status = self.POP_NIL

    def push(self, value: object):
        self.__stack.append(value)

    def pop(self):
        if self.size() > 0:
            _ = self.__stack.pop(-1)
            self.__pop_status = self.POP_OK
        else:
            self.__pop_status = self.POP_ERR

    def clear(self):
        self.__init__()

    def peek(self) -> object:
        if self.size() > 0:
            result = self.__stack[-1]
            self.__peek_status = self.PEEK_OK
        else:
            result = 0
            self.__peek_status = self.PEEK_ERR
        return result

    def size(self) -> int:
        return len(self.__stack)

    # status requests
    def get_pop_status(self) -> int:
        return self.__pop_status

    def get_peek_status(self) -> int:
        return self.__peek_status

