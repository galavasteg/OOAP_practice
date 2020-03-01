"""
AbstractDynamicArray is an abstract data type for
implementing a dynamic array.

CONSTANTS

    GETITEM_NIL = 0                # __getitem__() not called yet
    GETITEM_OK = 1                 # last __getitem__() call returned correct item
    GETITEM_TYPE_ERR = 2           # __getitem__() got wrong index(ices) type
    GETITEM_OUT_OF_BOUNDS_ERR = 3  # __getitem__() got wrong index(ices) value

    INSERT_NIL = 0         # insert() not called yet
    INSERT_OK = 1          # last insert() call completed successfully
    INSERT_TYPE_ERR = 2    # insert() got wrong index type
    INSERT_BOUNDS_ERR = 3  # last insert() failed with an GETITEM_*_ERR

    DELETE_NIL = 0         # delete() not called yet
    DELETE_OK = 1          # last delete() call completed successfully
    DELETE_TYPE_ERR = 2    # delete() got wrong index type
    DELETE_BOUNDS_ERR = 3  # last delete() failed with an GETITEM_*_ERR

ATTRIBUTES

    INITIAL_CAPACITY: int
        Initial capacity of the array

    MIN_CAPACITY: int
        Minimum capacity of the array.

    CAPACITY_MULTIPLIER: int
        Multiply capacity of the array by this value
        before insertion a new item to the array if it is full.

    CAPACITY_DELIMITER: int
        Divide capacity of the array by this value
        after deletion the item from the array if it is full
        by **DECREASE_CAPACITY_PERCENT_THRESHOLD**.

    DECREASE_CAPACITY_PERCENT_THRESHOLD: int
        Capacity fill percentage below which capacity divides
        by **CAPACITY_DELIMITER**.

CONSTRUCTOR

    __new__(cls) -> new dynamic array instance
        Post-condition:
            - created a new instance

    __init__(self, max_size: int):
        Initializing the instance after it's been created.

        Post-condition:
            - the array command statuses set to initial (*_NIL constants)
            - the array capacity set to **INITIAL_CAPACITY**
            - the array size is 0

COMMANDS

    insert(self, i: int item: object) - Insert **item** into **i**-th position.

        Pre-condition:
            - **i** points to existing item or equal to array size.
        Post-condition:
            - all subsequent items shifted forward
            - if the array is full before insertion command then
              this command multiplies capacity by **CAPACITY_MULTIPLIER**.

    delete(self, i: int) - Delete item in **i**-th position.

        Pre-condition:
            - **i** points to existing item.
        Post-condition:
            - all subsequent items shifted forward
            - if the array is less than
              **DECREASE_CAPACITY_PERCENT_THRESHOLD** % full
              after deletion then this command decrease capacity
              by **CAPACITY_DELIMITER**, but not less than
              **MIN_CAPACITY**.

ADDITIONAL COMMANDS

    append(self, item: object) - Add a new **item** to the array
                                 as the last item.
        Post-condition:
            - an item added to the array as the last item.

REQUESTS
    __len__(self) -> number of items in the array.

    __getitem__(self) -> existing item of the array by his **i** pointer.

        Pre-condition:
            - **i** points to existing item.

ADDITIONAL REQUESTS

    get_capacity(self) -> capacity of the array

STATUS REQUESTS

    get_getitem_status(self) - status of last __getitem__() call (GETITEM_* constant)
    get_insert_status(self) - status of last insert() call (INSERT_* constant)
    get_delete_status(self) - status of last delete() call (DELETE_* constant)

"""

from abc import ABCMeta, abstractmethod


class _BaseAbstractDynamicArray(metaclass=ABCMeta):

    GETITEM_NIL = 0                # __getitem__() not called yet
    GETITEM_OK = 1                 # last __getitem__() call returned correct item
    GETITEM_TYPE_ERR = 2           # __getitem__() got wrong index(ices) type
    GETITEM_OUT_OF_BOUNDS_ERR = 3  # __getitem__() got wrong index(ices) value

    INSERT_NIL = 0         # insert() not called yet
    INSERT_OK = 1          # last insert() call completed successfully
    INSERT_TYPE_ERR = 2    # insert() got wrong index type
    INSERT_BOUNDS_ERR = 3  # last insert() failed with an GETITEM_*_ERR

    DELETE_NIL = 0         # delete() not called yet
    DELETE_OK = 1          # last delete() call completed successfully
    DELETE_TYPE_ERR = 2    # delete() got wrong index type
    DELETE_BOUNDS_ERR = 3  # last delete() failed with an GETITEM_*_ERR

    @property
    @abstractmethod
    def INITIAL_CAPACITY(self) -> int:
        """Initial capacity of the array."""
        return 0

    @property
    @abstractmethod
    def MIN_CAPACITY(self) -> int:
        """Minimum capacity of the array."""
        return 0

    @property
    @abstractmethod
    def CAPACITY_MULTIPLIER(self) -> int:
        """Multiply capacity of the array by this value
        before insertion a new item to the array if it is full."""
        return 0

    @property
    @abstractmethod
    def CAPACITY_DELIMITER(self) -> int:
        """Divide capacity of the array by this value
        after deletion the item from the array if it is full
        by **DECREASE_CAPACITY_PERCENT_THRESHOLD**."""
        return 0

    @property
    @abstractmethod
    def DECREASE_CAPACITY_PERCENT_THRESHOLD(self) -> int:
        """Capacity fill percentage below which capacity divides
        by **CAPACITY_DELIMITER**."""
        return 0

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

    # commands:
    @abstractmethod
    def insert(self, i: int, item):
        """Insert **item** into **i**-th position.

        Pre-condition:
            - **i** points to existing item or equal to array size.
        Post-condition:
            - all subsequent items shifted forward
            - if the array is full before insertion command then
              this command multiplies capacity by **CAPACITY_MULTIPLIER**.

        """

    @abstractmethod
    def delete(self, i: int):
        """Delete item in **i**-th position.

        Pre-condition:
            - **i** points to existing item.
        Post-condition:
            - all subsequent items shifted forward
            - if the array is less than
              **DECREASE_CAPACITY_PERCENT_THRESHOLD** % full
              after deletion then this command decrease capacity
              by **CAPACITY_DELIMITER**, but not less than
              **MIN_CAPACITY**.

          """

    # additional commands:
    @abstractmethod
    def append(self, item: object):
        """Add a new **item** to the array as the last item.

        Post-condition:
            - an item added to the array as the last item.

        """

    # requests:
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the array."""
        return 0

    @abstractmethod
    def __getitem__(self, i: int) -> object:
        """Return existing item of the array by his **i** pointer.

        Pre-condition: **i** points to existing item.

        """
        return None

    # additional requests:
    def get_capacity(self) -> int:
        """Return capacity of the array"""
        return 0

    # command statuses requests:
    @abstractmethod
    def get_getitem_status(self) -> int:
        """Return status of last __getitem__() call:
        one of the GETITEM_* constants."""
        return 0

    @abstractmethod
    def get_insert_status(self) -> int:
        """Return status of last insert() call:
        one of the INSERT_* constants."""
        return 0

    @abstractmethod
    def get_delete_status(self) -> int:
        """Return status of last delete() call:
        one of the DELETE_* constants."""
        return 0


class AbstractDynamicArray(_BaseAbstractDynamicArray):
    ...


class AbstractSlicableDynamicArray(_BaseAbstractDynamicArray):
    """TODO: insert in tail if index is greater then size"""
    GETITEM_SLICE_OK = 2           # last __getitem__() call returned correct items
    GETITEM_TYPE_ERR = 3           # __getitem__() got wrong index(ices) type
    GETITEM_OUT_OF_BOUNDS_ERR = 4  # __getitem__() got wrong index(ices) value
    GETITEM_SLICE_TYPE_ERR = 5     # __getitem__() got wrong slice indices

    # requests:
    @abstractmethod
    def __getitem__(self, i: int or slice) -> object:
        """TODO: doc"""
        return None

