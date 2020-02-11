from .abstract_data_types.abstract_linked_list import AbstractLinkedList


class __ParentList(AbstractLinkedList):
    def __init__(self):
        """Implementation of an AbstractLinkedList."""
        super().__init__()
        self._cursor = None
        self.__storage = []
        self.__head_pointer = None
        self.__tail_pointer = None
        # last calls statuses
        self.__head_status = self.HEAD_NIL
        self.__tail_status = self.TAIL_NIL
        self.__right_status = self.RIGHT_NIL
        self.__put_right_status = self.PUT_RIGHT_NIL
        self.__put_left_status = self.PUT_LEFT_NIL
        self.__remove_status = self.REMOVE_NIL
        self.__get_status = self.GET_NIL
        self.__replace_status = self.REPLACE_NIL
        self.__find_status = self.FIND_NIL
        self.__remove_all_status = self.REMOVE_ALL_NIL


class LinkedList(__ParentList):
    ...


class TwoWayList(__ParentList):
    LEFT_NIL = 0        # left() not called yet
    LEFT_OK = 1         # last left() call completed successfully
    LEFT_EMPTY_ERR = 2  # storage is empty
    LEFT_HEAD_ERR = 3   # cursor is on the 1st node

    def __init__(self):
        super().__init__()
        self.__left_status = self.LEFT_NIL

    def get_left_status(self) -> int:
        return self.__left_status

