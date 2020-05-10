"""
This is a specification of the BloomFilter Abstract
Data Type.

CONSTRUCTOR

    __new__(cls) -> new instance
        Post-condition:
            - created a new instance.

    __init__(self, capacity: int):
        Initializing the instance after it's been created.

        Post-condition:
            - filter size is **size**.

COMMANDS

    add(self, value: object) - Map the **value** on the filter.

        Post-condition:
            - the **value** matches the filter.

REQUESTS

    get_size(self) -> filter size.

    is_value(self, value: str) -> is the **value** matches the filter?

"""

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

        """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
