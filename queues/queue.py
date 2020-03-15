from .abstract_data_types import AbstractQueue
from dynamic_array import DynamicArray


class Queue(AbstractQueue):

    def __init__(self):
        """Implementation of an AbstractQueue."""
        super().__init__()
        self.__queue = DynamicArray()

        self.__peek_status = self.PEEK_NIL
        self.__dequeue_status = self.DEQUEUE_NIL

    # commands:
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if len(self) == 0:
            self.__dequeue_status = self.DEQUEUE_EMPTY_ERR
        else:
            head_i = 0

            self.__queue.delete(head_i)

            self.__dequeue_status = self.DEQUEUE_OK

    # requests:
    def __len__(self):
        return len(self.__queue)

    def peek(self) -> object:
        if len(self) == 0:
            self.__peek_status = self.PEEK_EMPTY_ERR

            item = super().peek()
        else:
            head_i = 0
            item = self.__queue[head_i]

            self.__peek_status = self.PEEK_OK

        return item

    # command statuses requests:
    def get_peek_status(self) -> int:
        return self.__peek_status

    def get_dequeue_status(self) -> int:
        return self.__dequeue_status

