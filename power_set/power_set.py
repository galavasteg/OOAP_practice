"""

CONSTANTS

CONSTRUCTOR

COMMANDS

REQUESTS

STATUS REQUESTS

"""

from hash_table import HashTable


# TODO: Представьте АТД PowerSet как наследника
#  АТД HashTable -- с ограничением на максимальное
#  количество элементов в множестве.


class Set(HashTable):

    def __init__(self):
        """
        Initializing the instance after it's been created.

        """
