from .abstract_data_types.abstract_linked_list import (
    _BaseAbstractLinkedList,
    AbstractLinkedList,
    AbstractTwoWayList
)


class __ParentList(_BaseAbstractLinkedList):

    def __init__(self):
        """Implementation of a _BaseAbstractLinkedList."""
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

    # commands
    def head(self):
        if not self.is_value():
            self.__head_status = self.HEAD_EMPTY_ERR
        else:
            self._cursor = self.__head_pointer

            self.__head_status = self.HEAD_OK

    def tail(self):
        if not self.is_value():
            self.__tail_status = self.TAIL_EMPTY_ERR
        else:
            self._cursor = self.__tail_pointer

            self.__tail_status = self.TAIL_OK

    def right(self):
        if not self.is_value():
            self.__right_status = self.RIGHT_EMPTY_ERR
        elif self.is_tail():
            self.__right_status = self.RIGHT_TAIL_ERR
        else:

            self._cursor += 1

            self.__right_status = self.RIGHT_OK

    def put_right(self, value: object):
        if not self.is_value():
            self.__put_right_status = self.PUT_RIGHT_EMPTY_ERR
        else:
            new_item_pointer = self._cursor + 1
            self.__storage.insert(new_item_pointer, value)

            self.__tail_pointer += 1
            self.__put_right_status = self.PUT_RIGHT_OK

    def put_left(self, value: object):
        if not self.is_value():
            self.__put_left_status = self.PUT_LEFT_EMPTY_ERR
        else:
            if self.is_head():
                new_item_pointer = self.__head_pointer
            else:
                new_item_pointer = self._cursor
            self.__storage.insert(new_item_pointer, value)

            self._cursor += 1
            self.__tail_pointer += 1
            self.__put_left_status = self.PUT_LEFT_OK

    def remove(self):
        if not self.is_value():
            self.__remove_status = self.REMOVE_EMPTY_ERR
        else:
            old_size = self.get_size()

            _ = self.__storage.pop(self._cursor)

            if old_size == 1:
                self.__head_pointer = None
                self.__tail_pointer = None
                self._cursor = None
                self.__remove_status = self.REMOVE_OK_EMPTY
            elif self.is_tail():
                self.__tail_pointer -= 1
                self._cursor -= 1
                self.__remove_status = self.REMOVE_OK_LEFT
            else:
                self.__tail_pointer -= 1
                self.__remove_status = self.REMOVE_OK_RIGHT

    def clear(self):
        self.__init__()

    # additional commands:
    def add_tail(self, value: object):

        self.__storage.append(value)

        if not self.is_value():
            self.__head_pointer = self.__tail_pointer = 0
            self._cursor = 0
        else:
            self.__tail_pointer += 1

    def replace(self, value: object):
        if not self.is_value():
            self.__replace_status = self.REPLACE_EMPTY_ERR
        else:

            self.__storage[self._cursor] = value

            self.__replace_status = self.REPLACE_OK

    def find(self, value: object):
        if not self.is_value():
            self.__find_status = self.FIND_EMPTY
        elif self.is_tail():
            self.__find_status = self.FIND_NOT_FOUND
        else:

            self.right()
            while self.get() != value and not self.is_tail():
                self.right()

            found = self.get() == value
            if not found:
                self.__find_status = self.FIND_NOT_FOUND
            else:
                self.__find_status = self.FIND_OK

    def remove_all(self, value: object):
        self.head()
        self.__remove_all_status = self.REMOVE_ALL_NOTHING

        while self.is_value() and (not self.is_tail() or self.get() == value):
            found = self.get() == value
            if found:
                self.remove()
                self.__remove_all_status = self.REMOVE_ALL_OK
            else:
                self.right()

    # requests:
    def get(self) -> object:
        if not self.__storage:

            value = super().get()

            self.__get_status = self.GET_EMPTY_ERR
        else:

            value = self.__storage[self._cursor]

            self.__get_status = self.GET_OK
        return value

    def get_size(self) -> int:
        if self.is_value():
            size = 1 + self.__tail_pointer - self.__head_pointer
        else:
            size = 0
        return size

    # additional requests:
    def is_head(self) -> bool:
        return (self.is_value() and
                self._cursor == self.__head_pointer)

    def is_tail(self) -> bool:
        return (self.is_value() and
                self._cursor == self.__tail_pointer)

    def is_value(self) -> bool:
        return self._cursor is not None

    # command statuses requests:
    def get_head_status(self) -> int:
        return self.__head_status

    def get_tail_status(self) -> int:
        return self.__tail_status

    def get_right_status(self) -> int:
        return self.__right_status

    def get_put_right_status(self) -> int:
        return self.__put_right_status

    def get_put_left_status(self) -> int:
        return self.__put_left_status

    def get_remove_status(self) -> int:
        return self.__remove_status

    def get_get_status(self) -> int:
        return self.__replace_status

    def get_replace_status(self) -> int:
        return self.__replace_status

    def get_find_status(self) -> int:
        return self.__find_status

    def get_remove_all_status(self) -> int:
        return self.__remove_all_status


class LinkedList(__ParentList, AbstractLinkedList):

    def __init__(self):
        """Implementation of an AbstractLinkedList."""
        super().__init__()


class TwoWayList(__ParentList, AbstractTwoWayList):

    def __init__(self):
        """Implementation of an AbstractTwoWayList."""
        super().__init__()
        self.__left_status = self.LEFT_NIL

    def left(self):
        if not self.is_value():
            self.__left_status = self.LEFT_EMPTY_ERR
        elif self.is_head():
            self.__left_status = self.LEFT_HEAD_ERR
        else:

            self._cursor -= 1

            self.__left_status = self.LEFT_OK

    def get_left_status(self) -> int:
        return self.__left_status

