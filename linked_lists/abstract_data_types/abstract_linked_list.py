"""
AbstractLinkedList is an abstract data type for
implementing a linked list.

CONSTANTS
    HEAD_NIL = 0        # head() not called yet
    HEAD_OK = 1         # last head() call completed successfully
    HEAD_EMPTY_ERR = 2  # storage is empty

    TAIL_NIL = 0        # tail() not called yet
    TAIL_OK = 1         # last tail() call completed successfully
    TAIL_EMPTY_ERR = 2  # storage is empty

    RIGHT_NIL = 0        # right() not called yet
    RIGHT_OK = 1         # last right() call completed successfully
    RIGHT_EMPTY_ERR = 2  # storage is empty
    RIGHT_TAIL_ERR = 3   # cursor is on the last node

    PUT_RIGHT_NIL = 0        # put_right() not called yet
    PUT_RIGHT_OK = 1         # last put_right() call completed successfully
    PUT_RIGHT_EMPTY_ERR = 2  # storage is empty

    PUT_LEFT_NIL = 0        # put_left() not called yet
    PUT_LEFT_OK = 1         # last put_left() call completed successfully
    PUT_LEFT_EMPTY_ERR = 2  # storage is empty

    REMOVE_NIL = 0        # remove() not called yet
    REMOVE_OK = 1         # last remove() call completed successfully
    REMOVE_EMPTY_ERR = 2  # storage is empty

    GET_NIL = 0        # get() not called yet
    GET_OK = 1         # last get() call returned correct item
    GET_EMPTY_ERR = 2  # storage is empty

    REPLACE_NIL = 0        # replace() not called yet
    REPLACE_OK = 1         # last replace() call completed successfully
    REPLACE_EMPTY_ERR = 2  # storage is empty

    FIND_NIL = 0        # find() not called yet
    FIND_OK = 1         # last find() call set the cursor to the next found node
    FIND_NOT_FOUND = 2  # last find() call found nothing
    FIND_EMPTY = 3      # storage is empty

    REMOVE_ALL_NIL = 0      # remove_all() not called yet
    REMOVE_ALL_OK = 1       # last remove_all() call remove items from storage
    REMOVE_ALL_NOTHING = 2  # last remove_all() call remove nothing

CONSTRUCTOR
    __new__(cls, max_size: int) -> new linked-list instance
        Post-condition:
            created a new instance with empty storage

    __init__(self, max_size: int):
        Initializing the instance after it's been created.
        Post-condition:
            The stack storage capacity is limited to *max_size* number
            of items

COMMANDS
    head(self) - Move cursor to the 1st node.
        Pre-condition:
            storage is not empty.
        Post-condition:
            cursor is on the 1st node.

    tail(self) - Move cursor to the last node.
        Pre-condition:
            storage is not empty.
        Post-condition:
            cursor is on the last node.

    right(self) - Move cursor to node right.
        Pre-conditions:
            - storage is not empty.
            - cursor is not on the last node;
        Post-condition:
            cursor is on the node to the right.

    put_right(self, value: object) - Put a new node with the *value* to
                                     the right of the node the cursor on.
        Pre-condition:
            storage is not empty.
        Post-condition:
            a new node with the *value* is in the storage to the right of
            the node the cursor on.

    put_left(self, value: object) - Put a new node with the *value* to
                                    the left of the node the cursor on.
        Pre-condition:
            storage is not empty.
        Post-condition:
            a new node with the *value*
            is in the storage to the left of
            the node the cursor on.

    remove(self) - Remove the node the cursor on from the storage.
                   The cursor sets to the right (priority) or
                   to the left node if they exist.
        Pre-condition:
            storage is not empty.
        Post-condition:
            - the node the cursor on removed from the storage
            - the cursor set to the right (priority) or
              to the left node if they exist.

    clear(self)
        Post-condition:
            storage is empty.

ADDITIONAL COMMANDS
    add_tail(self, value: object) - Add a new node with the *value*
                                    to the storage as the last item.
        Post-condition:
            a new node with the *value* added to the storage as the
            last item.

    replace(self, value: object) - Place a new *value* to the node
                                   the cursor on.
        Pre-condition:
            storage is not empty.
        Post-condition:
            the node the cursor on contain a new *value*

    find(self, value: object) - Set the cursor to the next node
                                with the searched *value* relative
                                to the node the cursor on.
        Post-condition:
            the cursor set to the next node with the searched
            *value* relative to the node the cursor on.

    remove_all(self, value: object) - Remove all nodes with the *value*
                                      from the storage.
        Post-condition:
            all nodes with the *value* removed from the storage.

REQUESTS
    get(self) -> value of the node the cursor on
        Pre-condition:
            storage is not empty.

    get_size(self) -> number of items in the storage

ADDITIONAL REQUESTS
    is_head(self) - the cursor is on the 1st storage item?
    is_tail(self) - the cursor is on the last storage item?
    is_value(self) - the cursor is on the node?
                     (equivalent) is the storage not empty?

STATUS REQUESTS
    get_head_status(self) - status of last head() call (PUSH_* constant)
    get_tail_status(self) - status of last tail() call (TAIL_* constant)
    get_right_status(self) - status of last right() call (RIGHT_* constant)
    get_put_right_status(self) - status of last put_right() call (PUT_RIGHT_* constant)
    get_put_left_status(self) - status of last put_left() call (PUT_LEFT_* constant)
    get_remove_status(self) - status of last remove() call (REMOVE_* constant)
    get_get_status(self) - status of last get() call (GET_* constant)
    get_replace_status(self) - status of last replace() call (REPLACE_* constant)
    get_find_status(self) - status of last find() call (FIND_* constant)
    get_remove_all_status(self) - status of last remove_all() call (REMOVE_ALL_* constant)

"""

# TODO: EN
"""
Почему операция tail не сводима к другим операциям (если исходить
из эффективной реализации)?

ANSWER:
Эффективная реализация подразумевает в идеале сложность О(1). Для метода
tail() достичь такой эффективности  можно прямым доступом к "хвосту",
поэтому делать метод НЕатамарным нет смысла. Достичь "хвоста" можно,
например, комбинацией методов right() и is_tail(): сложность О(n),
больше действий, один из методов также неатамарный - данное решение
менее эффективно.

Операция поиска всех узлов с заданным значением, выдающая список
таких узлов, уже не нужна. Почему?

ANSWER:
Вместо такой операции введена логика последовательного
перемещения курсора к следующему искомому элементу с нужным значением.
"""


from abc import ABCMeta, abstractmethod


class _BaseAbstractLinkedList(metaclass=ABCMeta):
    HEAD_NIL = 0        # head() not called yet
    HEAD_OK = 1         # last head() call completed successfully
    HEAD_EMPTY_ERR = 2  # storage is empty

    TAIL_NIL = 0        # tail() not called yet
    TAIL_OK = 1         # last tail() call completed successfully
    TAIL_EMPTY_ERR = 2  # storage is empty

    RIGHT_NIL = 0        # right() not called yet
    RIGHT_OK = 1         # last right() call completed successfully
    RIGHT_EMPTY_ERR = 2  # storage is empty
    RIGHT_TAIL_ERR = 3   # cursor is on the last node

    PUT_RIGHT_NIL = 0        # put_right() not called yet
    PUT_RIGHT_OK = 1         # last put_right() call completed successfully
    PUT_RIGHT_EMPTY_ERR = 2  # storage is empty

    PUT_LEFT_NIL = 0        # put_left() not called yet
    PUT_LEFT_OK = 1         # last put_left() call completed successfully
    PUT_LEFT_EMPTY_ERR = 2  # storage is empty

    REMOVE_NIL = 0        # remove() not called yet
    REMOVE_OK_RIGHT = 1   # item remove()'ed successfully, cursor set to right node
    REMOVE_OK_LEFT = 2    # item remove()'ed successfully, cursor set to left node
    REMOVE_OK_EMPTY = 3   # item remove()'ed successfully, cursor not set: storage is empty
    REMOVE_EMPTY_ERR = 4  # storage is empty

    GET_NIL = 0        # get() not called yet
    GET_OK = 1         # last get() call returned correct item
    GET_EMPTY_ERR = 2  # storage is empty

    REPLACE_NIL = 0        # replace() not called yet
    REPLACE_OK = 1         # last replace() call completed successfully
    REPLACE_EMPTY_ERR = 2  # storage is empty

    FIND_NIL = 0        # find() not called yet
    FIND_OK = 1         # last find() call set the cursor to the next found node
    FIND_EMPTY = 2      # storage is empty
    FIND_NOT_FOUND = 3  # there is no next node with the *value*

    REMOVE_ALL_NIL = 0      # remove_all() not called yet
    REMOVE_ALL_OK = 1       # last remove_all() call remove items from storage
    REMOVE_ALL_NOTHING = 2  # last remove_all() call remove nothing

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

    # commands
    @abstractmethod
    def head(self):
        """
        Move cursor to the 1st node.
        Pre-condition: storage is not empty.
        Post-condition: cursor is on the 1st node.
        """

    @abstractmethod
    def tail(self):
        """
        Move cursor to the last node.
        Pre-condition: storage is not empty.
        Post-condition: cursor is on the last node.
        """

    @abstractmethod
    def right(self):
        """
        Move cursor to node right.
        Pre-conditions:
            - storage is not empty.
            - cursor is not on the last node;
        Post-condition: cursor is on the node to the right.
        """

    @abstractmethod
    def put_right(self, value: object):
        """
        Put a new node with the *value* to the right
        of the node the cursor on.
        Pre-condition: storage is not empty.
        Post-condition: a new node with the *value*
            is in the storage to the right of
            the node the cursor on.
        """

    @abstractmethod
    def put_left(self, value: object):
        """
        Put a new node with the *value* to the left
        of the node the cursor on.
        Pre-condition: storage is not empty.
        Post-condition: a new node with the *value*
            is in the storage to the left of
            the node the cursor on.
        """

    @abstractmethod
    def remove(self):
        """
        Remove the node the cursor on from the storage.
        The cursor sets to the right (priority) or
        to the left node if they exist.
        Pre-condition: storage is not empty.
        Post-condition:
            - the node the cursor on removed from the storage
            - the cursor set to the right (priority) or
              to the left node if they exist.
        """

    @abstractmethod
    def clear(self):
        """Post-condition: storage is empty."""

    # additional commands:
    @abstractmethod
    def add_tail(self, value: object):
        """Add a new node with the *value* to the storage
        as the last item."""

    @abstractmethod
    def replace(self, value: object):
        """
        Place a new *value* to the node the cursor on.
        Pre-condition: storage is not empty.
        Post-condition:
            the node the cursor on contain a new *value*
        """

    @abstractmethod
    def find(self, value: object):
        """
        Set the cursor to the next node with the
        searched *value* relative to the node
        the cursor on.
        Post-condition:
            the cursor set to the next node with the searched
            *value* relative to the node the cursor on.
        """

    @abstractmethod
    def remove_all(self, value: object):
        """
        Remove all nodes with the *value* from the storage.
        Post-condition:
            all nodes with the *value* removed from the storage.
        """

    # requests:
    @abstractmethod
    def get(self) -> object:
        """
        Get the value of node the cursor on.
        Pre-condition: storage is not empty.
        """
        return 0

    @abstractmethod
    def get_size(self) -> int:
        """Return the number of items in the storage"""
        return 0

    # additional requests:
    @abstractmethod
    def is_head(self) -> bool:
        """Return True if the cursor is on the 1st
        storage item."""
        return False

    @abstractmethod
    def is_tail(self) -> bool:
        """Return True if the cursor is on the last
        storage item."""
        return False

    @abstractmethod
    def is_value(self) -> bool:
        """Return True if the cursor is on the node.
        Can be used to check the storage is not empty."""
        return False

    # command statuses requests:
    @abstractmethod
    def get_head_status(self) -> int:
        """Return status of last head() call:
        one of the HEAD_* constants."""
        return 0

    @abstractmethod
    def get_tail_status(self) -> int:
        """Return status of last tail() call:
        one of the TAIL_* constants."""
        return 0

    @abstractmethod
    def get_right_status(self) -> int:
        """Return status of last right() call:
        one of the RIGHT_* constants."""
        return 0

    @abstractmethod
    def get_put_right_status(self) -> int:
        """Return status of last put_right() call:
        one of the PUT_RIGHT_* constants."""
        return 0

    @abstractmethod
    def get_put_left_status(self) -> int:
        """Return status of last put_left() call:
        one of the PUT_LEFT_* constants."""
        return 0

    @abstractmethod
    def get_remove_status(self) -> int:
        """Return status of last remove() call:
        one of the REMOVE_* constants."""
        return 0

    @abstractmethod
    def get_get_status(self) -> int:
        """Return status of last get() call:
        one of the GET_* constants."""
        return 0

    @abstractmethod
    def get_replace_status(self) -> int:
        """Return status of last replace() call:
        one of the REPLACE_* constants."""
        return 0

    @abstractmethod
    def get_find_status(self) -> int:
        """Return status of last find() call:
        one of the FIND_* constants."""
        return 0

    @abstractmethod
    def get_remove_all_status(self) -> int:
        """Return status of last remove_all() call:
        one of the REMOVE_ALL* constants."""
        return 0


class AbstractLinkedList(_BaseAbstractLinkedList):
    ...


class AbstractTwoWayList(_BaseAbstractLinkedList):
    LEFT_NIL = 0        # left() not called yet
    LEFT_OK = 1         # last left() call completed successfully
    LEFT_EMPTY_ERR = 2  # storage is empty
    LEFT_HEAD_ERR = 3   # cursor is on the 1st node

    @abstractmethod
    def left(self):
        """
        Move cursor to node left.
        Pre-conditions:
            - storage is not empty.
            - cursor is not on the 1st node;
        Post-condition: cursor is on the node to the left.
        """

    @abstractmethod
    def get_left_status(self) -> int:
        return 0

