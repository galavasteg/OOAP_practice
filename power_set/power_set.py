"""
This is a specification of the PowerSet Abstract Data
Type (2). It extends HashTable ADT (1) with the following
methods: intersection, union, difference, is_subset.

--------------------- (1) HashTable ADT ---------------------

CONSTANTS

    PUT_NIL            # put() not called yet
    PUT_OK             # last put() call completed successfully
    PUT_FULL_ERR       # hashtable is full
    PUT_EXISTS_ERR     # the value is already in the hashtable

    REMOVE_NIL          # remove() not called yet
    REMOVE_OK           # last remove() call completed successfully
    REMOVE_NOVALUE_ERR  # no value in the hashtable

CONSTRUCTOR

    __new__(cls) -> new instance
        Post-condition:
            - created a new instance.

    __init__(self, capacity: int):
        Initializing the instance after it's been created.

        Post-condition:
            - method statuses set to initial (*_NIL constants).
            - max number of values in the hashtable is **capacity**.
            - values count in the hashtable is 0.

COMMANDS
    put(self, value: object) - Put **value** in the hashtable.

        Pre-condition:
            - the hashtable is not full.
            - **value** does not exist in hashtable.
        Post-condition:
            - the **value** was  put in the hashtable.

    remove(self, value: str) - Remove **value** from the hashtable.

        Pre-condition:
            - **value** exists in the hashtable.
        Post-condition:
            - **value** removed from hashtable.

REQUESTS

    __len__(self) -> number of values in the hashtable.

    _hash_func(self, value) -> **value** slot.

    get_capacity(self) -> max number of values in the hashtable.

    is_value(self, value) -> is the **value** in the hashtable?

STATUS REQUESTS
    get_put_status(self) -> status of last put() call (PUT_* constant).
    get_remove_status(self) -> status of last remove() call (REMOVE_* constant).


--------------------- (2) PowerSet ADT ---------------------

REQUESTS

    intersection(self, with_set) -> a set of a **self**-set elements that also belong to with_set.

    union(self, with_set) -> a set of all elements in both sets.

    difference(self, with_set) -> a set of elements in a **self**-set but not in **with_set**.

    is_subset(self, of_set) -> are all the elements in a **self**-set in **of_set**?

"""

from itertools import chain, filterfalse

from hash_table import HashTable


class PowerSet(HashTable):

    # additional requests:
    def __iter__(self):  # -> typing.Iterator[str]
        """
        Iterate over values in a set.

        """
        yield from filter(None, self._values)

    def __repr__(self) -> str:
        """
        Represent values of a set.

        """
        s = '{%s}' % ', '.join(map(repr, self))
        return s

    # requests:
    def intersection(self, with_set: 'PowerSet') -> 'PowerSet':
        """
        Return a set of a **self**-set elements that
        also belong to **with_set**.

        """
        intersection_set = self.__class__(self.get_capacity())

        for value in filter(self.is_value, with_set):
            intersection_set.put(value)

        return intersection_set

    def union(self, with_set: 'PowerSet') -> 'PowerSet':
        """
        Return a set of all elements in both sets.

        """
        union_count = len(self) + len(with_set)
        capacity = self.get_capacity()
        if union_count > capacity:
            capacity = union_count
        union_set = self.__class__(capacity)

        for value in chain(self, with_set):
            union_set.put(value)

        return union_set

    def difference(self, with_set: 'PowerSet') -> 'PowerSet':
        """
        Return a set of elements in a **self**-set but
        not in **with_set**.

        """
        diff_set = self.__class__(self.get_capacity())

        for value in filterfalse(with_set.is_value, self):
            diff_set.put(value)

        return diff_set

    def is_subset(self, of_set: 'PowerSet') -> bool:
        """
        Check if all elements in a **self**-set are in **of_set**.

        """
        is_subset = all(map(of_set.is_value, self))
        return is_subset
