import ctypes
from collections.abc import Iterable

from .abstract_data_types import AbstractQueue


class Queue(AbstractQueue):

    def __init__(self):
        """Implementation of an AbstractDynamicArray."""
        super().__init__()

