"""
This is an abstract data type specification for
a HashTable implementation.

CONSTANTS

CONSTRUCTOR

COMMANDS

REQUESTS

STATUS REQUESTS

"""

from itertools import chain


class HashTable:

    PUT_NIL = 0
    PUT_OK = 1
    PUT_FULL_ERR = 2
    PUT_EXISTS_ERR = 3
    PUT_COLLISION_ERR = 4

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_NOVALUE_ERR = 2

    STEP = 5

    def __init__(self, capacity: int):
        """

        """
        self._capacity = capacity
        self._values = [None] * self._capacity

        self._put_status = self.PUT_NIL
        self._remove_status = self.REMOVE_NIL

    # additional requests:
    def _hash_func(self, value: str) -> int:
        bStr = value.encode()
        slot = sum(bStr) % self._capacity
        return slot

    def _next_busy_slot_stepper(self, start_slot: int):
        """"""
        yield start_slot

        tmp_slot = start_slot + self.STEP
        within = tmp_slot < self._capacity
        is_busy = within and self._values[tmp_slot] is not None

        while is_busy:
            yield tmp_slot

            tmp_slot += self.STEP
            within = tmp_slot < self._capacity
            is_busy = within and self._values[tmp_slot] is not None



    def _is_collision(self, of_slot: int, slot: int) -> bool:
        slot_value = self._values[slot]
        is_collision = self._hash_func(slot_value) == of_slot
        return is_collision

    def _get_last_collision_slot(self, of_slot: int, slots: tuple) -> tuple:
        is_collision = lambda s: self._is_collision(of_slot, slot=s)
        last_collision_slot = next(filter(is_collision, reversed(slots)),
                                   None)
        return last_collision_slot

    def _get_collision_slots(self, of_slot: int, slots: tuple) -> tuple:
        collision_slots = []

        slots_ = slots
        of_slot_ = of_slot

        while slots_:
            of_slot_ = last_collision_slot = self._get_last_collision_slot(
                    of_slot_, slots_)

            if last_collision_slot:
                collision_slots.append(last_collision_slot)

                from_slot = slots.index(last_collision_slot) + 1
            else:
                from_slot = len(slots)
            slots_ = slots[from_slot:]

        return tuple(collision_slots)

    # commands:
    def put(self, value: str):
        """
        Store **value** into hashtable.

        Pre-condition:
            - the hashtable is not full
            - **value** does not exist in hashtable
            - no collision resolution error
        Post-condition:
            - **value** added to hashtable.

        """
        if len(self) >= self._capacity:
            self._put_status = self.PUT_FULL_ERR
        else:
            self._put_status = self.PUT_COLLISION_ERR

            hash_slot = self._hash_func(value)
            for slot in self._slots_stepper(hash_slot):

                if self._values[slot] == value:
                    self._put_status = self.PUT_EXISTS_ERR
                    break

                is_free = self._values[slot] is None
                if is_free:
                    self._values[slot] = value
                    self._put_status = self.PUT_OK

    def remove(self, value: str):
        """
        Remove **value** from the hashtable.

        Pre-condition:
            - **value** exists in the hashtable
        Post-condition:
            - **value** removed from the hashtable

        """
        hash_slot = self._hash_func(value)
        slots_stepper = self._next_busy_slot_stepper(hash_slot)

        self._remove_status = self.REMOVE_NOVALUE_ERR

        for to_remove_slot in slots_stepper:
            if self._values[to_remove_slot] == value:

                next_busy_stepped_slots = tuple(slots_stepper)
                collision_slots = self._get_collision_slots(
                        of_slot=to_remove_slot,
                        slots=next_busy_stepped_slots)

                if collision_slots:
                    # offset collisions
                    to_resolve_slots = (to_remove_slot,) + collision_slots
                    for replace_s, by_s in zip(to_resolve_slots,
                                               to_resolve_slots[1:]):
                        self._values[replace_s] = self._values[by_s]
                    self._values[collision_slots[-1]] = None
                else:
                    self._values[to_remove_slot] = None

                self._remove_status = self.REMOVE_OK

    # requests:
    def __len__(self):
        return len(tuple(filter(None.__ne__, self._values)))

    def is_value(self, value: str) -> bool:
        is_value = False

        hash_slot = self._hash_func(value)
        for slot in self._next_busy_slot_stepper(hash_slot):

            is_value = self._values[slot] == value
            if is_value:
                break

        return is_value

    def get_capacity(self):
        """Return hashtable capacity."""
        return self._capacity

    # method statuses requests:
    def get_put_status(self) -> int:
        """Return status of last put() call:
        one of the PUT_* constants."""
        return self._put_status

    def get_remove_status(self) -> int:
        """Return status of last remove() call:
        one of the REMOVE_* constants."""
        return self._remove_status
