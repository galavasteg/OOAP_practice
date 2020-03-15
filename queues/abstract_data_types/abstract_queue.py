"""
"""

from abc import ABCMeta, abstractmethod


class AbstractQueue(metaclass=ABCMeta):

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

