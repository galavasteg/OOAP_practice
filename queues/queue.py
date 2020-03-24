from .abstract_data_types import AbstractQueue
from dynamic_array import DynamicArray


class Queue(AbstractQueue):

    def __init__(self):
        """Implementation of an AbstractQueue."""
        super().__init__()
        self.__queue = DynamicArray()

        self.__get_status = self.GET_NIL
        self.__remove_status = self.REMOVE_NIL

    # commands:
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if len(self) == 0:
            self.__remove_status = self.REMOVE_EMPTY_ERR
        else:
            head_i = 0

            self.__queue.delete(head_i)

            self.__remove_status = self.REMOVE_OK

    # requests:
    def __len__(self):
        return len(self.__queue)

    def get_front(self) -> object:
        if len(self) == 0:
            self.__get_status = self.GET_EMPTY_ERR

            item = super().get_front()
        else:
            head_i = 0
            item = self.__queue[head_i]

            self.__get_status = self.GET_OK

        return item

    # command statuses requests:
    def get_get_status(self) -> int:
        return self.__get_status

    def get_remove_status(self) -> int:
        return self.__remove_status

