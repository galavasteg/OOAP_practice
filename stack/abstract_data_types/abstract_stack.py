"""
AbstractStack is an abstract data type for stack implementation.

CONSTANTS
    POP_NIL = 0   # pop() not called yet

    POP_OK = 1    # last pop() call completed successfully

    POP_ERR = 2   # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet

    PEEK_OK = 1   # last call peek() returned correct item

    PEEK_ERR = 2  # stack storage is empty

CONSTRUCTOR
    __new__(cls) -> new class instance
        Post-condition:
            created a new empty stack instance.

        NOTE: __new__ is NOT abstract method. You shouldn't
            need to override __new__. See:
            https://mail.python.org/pipermail/tutor/2008-April/061426.html

    __init__(self):
        Initializing the instance after it's been created.

"""

from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):
    POP_NIL = 0  # pop() not called yet
    POP_OK = 1   # last pop() call completed successfully
    POP_ERR = 2  # stack storage is empty

    PEEK_NIL = 0  # peek() not called yet
    PEEK_OK = 1   # last peek() call returned correct item
    PEEK_ERR = 2  # stack storage is empty

    # constructor
    def __new__(cls) -> object:
        """
        Create a class instance
        Post-condition:
            created a new empty stack instance

        NOTE: __new__ is NOT abstract method. You shouldn't
            need to override __new__. See:
            https://mail.python.org/pipermail/tutor/2008-April/061426.html
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """Initializing the instance after it's been created"""


