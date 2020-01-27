"""
AbstractLinkedList is an abstract data type for
implementing a linked list.

CONSTRUCTOR
    __new__(cls, max_size: int) -> new linked-list instance
        Post-condition:
            created a new instance with empty storage

    __init__(self, max_size: int):
        Initializing the instance after it's been created.
        Post-condition:
            The stack storage capacity is limited to *max_size* number
            of items

"""

from abc import ABCMeta, abstractmethod


class AbstractLinkedList(metaclass=ABCMeta):

    # constructor
    def __new__(cls) -> object:
        """
        Create a class instance
        Post-condition: created a new instance with empty storage
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """Initializing the instance after it's been created"""

