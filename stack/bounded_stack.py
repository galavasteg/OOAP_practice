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

    def __init__(self, max_size: int = None):
        """The BoundedStack class implements AbstractBoundedStack.

        :param max_size: (optional) maximum possible number of
            items in the stack storage. 32 by default. The default
            value can be changed by calling
            set_def_max_size(*new_default_val*) before creating
            the stack instance.
        """

        super().__init__(max_size)

        # private attributes
        self.__max_size = (self.__DEFAULT_MAX_SIZE if max_size is None
                           else max_size)  # stack storage size limit
        self.__stack = []  # empty list main stack storage

        # initial statuses for peek(), pop() and push() pre-conditions
        self.__peek_status = self.PEEK_NIL  # peek() last call status
        self.__pop_status = self.POP_NIL    # pop() last call status
        self.__push_status = self.PUSH_NIL  # push() last call status

    def push(self, value: object):
        if self.size < self.__max_size:
            self.__stack.append(value)
            self.__push_status = self.PUSH_OK
        else:
            self.__push_status = self.PUSH_ERR

    def pop(self):
        if self.size > 0:
            _ = self.__stack.pop(-1)
            self.__pop_status = self.POP_OK
        else:
            self.__pop_status = self.POP_ERR

    def clear(self):
        """Reset stack to initial state. *max_size* will
        not be changed even if set_def_max_size() was
        called earlier"""
        max_size = self.get_max_size()
        self.__init__(max_size)

    def peek(self) -> object:
        if self.size > 0:
            result = self.__stack[-1]
            self.__peek_status = self.PEEK_OK
        else:
            result = 0
            self.__peek_status = self.PEEK_ERR
        return result

    @classmethod
    def set_def_max_size(cls, value: int):
        """Set the default maximum possible number of items
        in the stack storage. New *value* will be implemented
        to stack-instances created after this command.

        :param value: maximum possible number of items in the
            stack storage
        """
        cls.__DEFAULT_MAX_SIZE = value

    @classmethod
    def get_def_max_size(cls) -> int:
        return cls.__DEFAULT_MAX_SIZE

    def get_current_size(self) -> int:
        return len(self.__stack)

    @property
    def size(self):
        return self.get_current_size()

    def get_max_size(self) -> int:
        return self.__max_size

    # status requests
    def get_pop_status(self) -> int:
        return self.__pop_status

    def get_peek_status(self) -> int:
        return self.__peek_status

    def get_push_status(self) -> int:
        return self.__push_status

