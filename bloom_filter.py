"""
This is a specification of the BloomFilter Abstract
Data Type.

CONSTRUCTOR

    __new__(cls) -> new instance
        Post-condition:
            - created a new instance.

    __init__(self, size: int):
        Initializing the instance after it's been created.

        Post-condition:
            - filter size is **size**.

COMMANDS

    add(self, value: object) - Map the **value** on the filter.

        Post-condition:
            - the **value** matches the filter.

REQUESTS

    get_size(self) -> filter size.

    is_value(self, value: object) -> is the **value** matches the filter?

"""

import operator
from functools import reduce


class BloomFilter:

    def __init__(self, size: int):
        """
        Initializing the instance after it's been created.

        Post-condition:
            - filter size is **size**.

        :param size: filter size.

        """
        assert size > 0, 'The size must greater than 0.'
        self._busy_bit_set = set()
        self._size = size

    # additional requests:
    def __or__(self, b_filter: 'BloomFilter') -> 'BloomFilter':
        """
        Return new filter as a union of this and **b_filter**.
        Both filters must be the same size.

        :param b_filter: a BloomFilter the size of this filter
        :return: new BloomFilter.

        >>> bf1, bf2 = BloomFilter(6), BloomFilter(6)
        >>> bf1.add('foo')
        >>> bf2.add('bar')
        >>> bf3 = bf1 | bf2
        >>> print('%s | %s = %s' % tuple(
        ...         bf._get_bit_mask() for bf
        ...         in (bf1, bf2, bf3)))
        000001 | 001010 = 001011

        """
        assert self._size == b_filter._size
        new_filter = type(self)(self._size)

        new_filter._busy_bit_set = self._busy_bit_set.union(
                b_filter._busy_bit_set)

        return new_filter

    def _get_bit_mask(self) -> str:
        """
        Return the filter bit mask.

        :return: bit mask of this filter.

        >>> bf = BloomFilter(5)
        >>> bf._get_bit_mask()
        '00000'
        >>> bf.add('foo')
        >>> bf._get_bit_mask()
        '10010'

        """
        mask = bin(reduce(operator.or_,
                          (2**b for b in self._busy_bit_set),
                          2**self._size))
        clean_mask = mask[3:]  # cut off '0b1...'
        return clean_mask

    def _hash1(self, value: str) -> int:
        """
        Map the **value** to the bit position on the
        filter bit mask.

        :param value: string.
        :return: bit position as positive integer.

        >>> BloomFilter(5)._hash1('foo')
        1

        """
        multiplier = 17

        def renew_hash(prev_hash: int, char: str) -> int:
            accum_hash = prev_hash * multiplier + ord(char)
            hash_ = accum_hash % self._size
            return hash_
        hash_ = reduce(renew_hash, value, 0)

        return hash_

    def _hash2(self, value: str) -> int:
        """
        Map the **value** to the bit position on the
        filter bit mask.

        :param value: string.
        :return: bit position as positive integer.

        >>> BloomFilter(5)._hash2('foo')
        4

        """
        b_str = value.encode()
        hash_ = sum(b_str) % self._size
        return hash_

    def _get_value_bit_positions(self, value: str) -> tuple:
        """
        Return mapped **value** on the filter bit mask
        with the hash* functions.

        :param value: string value.
        :return: a set of bits.

        >>> bf = BloomFilter(5)
        >>> bf.add('foo')
        >>> bf._get_value_bit_positions('foo')
        (1, 4)
        >>> bf._get_bit_mask()
        '10010'

        """
        hashes = (
            self._hash1(value),
            self._hash2(value),
        )
        return hashes

    # commands:
    def add(self, value: str) -> None:
        """
        Map the **value** on the filter.

        Post-condition:
            - the **value** matches the filter.

        :param value: string.

        >>> bf = BloomFilter(5)
        >>> bf.add('foo')
        >>> bf.is_value('foo'), bf._get_bit_mask()
        (True, '10010')

        """
        bits = self._get_value_bit_positions(value)
        self._busy_bit_set.update(bits)

    # requests:
    def get_size(self) -> int:
        """
        Return filter size.

        >>> BloomFilter(4).get_size()
        4

        """
        return self._size

    def is_value(self, value: str) -> bool:
        """
        Check if the **value** matches the filter.

        :param value: string.

        >>> bf = BloomFilter(4)
        >>> bf.add('foo')
        >>> bf.is_value('foo')
        True
        >>> bf.is_value('bar')
        False
        >>> bf.is_value('')  # false positive
        True

        """
        bits = self._get_value_bit_positions(value)
        is_value = self._busy_bit_set.issuperset(bits)
        return is_value


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
