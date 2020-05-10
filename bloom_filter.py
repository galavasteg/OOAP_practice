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

class BloomFilter:

    def __init__(self, size: int):
        """
        Initializing the instance after it's been created.

        Post-condition:
            - filter size is **size**.

        :param size: filter size.

        """

    # commands:
    def add(self, value: str) -> None:
        """
        Map the **value** on the filter.

        Post-condition:
            - the **value** matches the filter.

        :param value: string.

        """

    # requests:
    def get_size(self) -> int:
        """
        Return filter size.
        """

    def is_value(self, value: str) -> bool:
        """
        Check if the **value** matches the filter.

        :param value: string.

        """
