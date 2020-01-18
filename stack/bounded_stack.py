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


