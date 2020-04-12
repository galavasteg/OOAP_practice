"""
This is an abstract data type specification for
a HashTable implementation.

CONSTANTS

    PUT_NIL            # put() not called yet
    PUT_OK             # last put() call completed successfully
    PUT_FULL_ERR       # hashtable is full
    PUT_EXISTS_ERR     # the value is already in the hashtable
    PUT_COLLISION_ERR  # can not put because of collisions

    REMOVE_NIL          # remove() not called yet
    REMOVE_OK           # last remove() call completed successfully
    REMOVE_NOVALUE_ERR  # no value in the hashtable

CONSTRUCTOR

    __new__(cls) -> new queue instance
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
            - no collision resolution error.
        Post-condition:
            - the **value** was  put in the hashtable.

    remove(self) - Remove **value** from the hashtable.

        Pre-condition:
            - **value** exists in the hashtable.
        Post-condition:
            - **value** removed from hashtable.

REQUESTS

    __len__(self) -> number of values in the hashtable.

    _hash_func(self, value: str) -> **value** slot.

    get_capacity(self) -> max number of values in the hashtable.

    is_value(self, value: str) -> is the **value** in the hashtable?

STATUS REQUESTS
    get_put_status(self) -> status of last put() call (PUT_* constant).
    get_remove_status(self) -> status of last remove() call (REMOVE_* constant).

"""

from itertools import chain


class HashTable:

    PUT_NIL = 0            # put() not called yet
    PUT_OK = 1             # last put() call completed successfully
    PUT_FULL_ERR = 2       # hashtable is full
    PUT_EXISTS_ERR = 3     # the value is already in the hashtable
    PUT_COLLISION_ERR = 4  # can not put because of collisions

    REMOVE_NIL = 0          # remove() not called yet
    REMOVE_OK = 1           # last remove() call completed successfully
    REMOVE_NOVALUE_ERR = 2  # no value in the hashtable

    def __init__(self, capacity: int):
        """
        Initializing the instance after it's been created.

        Post-condition:
            - method statuses set to initial (*_NIL constants).
            - max number of values in the hashtable is **capacity**.
            - values count in the hashtable is 0.

        """
        self._capacity = capacity
        self._values = [None] * self._capacity

        self.step = 5

        self._put_status = self.PUT_NIL
        self._remove_status = self.REMOVE_NIL

    # additional requests:
    def _next_busy_slot_stepper(self, start_slot: int):
        """"""
        yield start_slot

        tmp_slot = start_slot + self.step
        within = tmp_slot < self._capacity
        is_busy = within and self._values[tmp_slot] is not None

        while is_busy:
            yield tmp_slot

            tmp_slot += self.step
            within = tmp_slot < self._capacity
            is_busy = within and self._values[tmp_slot] is not None

    def _to_free_slot_stepper(self, start_slot: int):
        for slot in chain((start_slot,),
                          self._next_busy_slot_stepper(start_slot)):
            yield slot

        slot += self.step
        is_free = (slot < self._capacity and
                   self._values[slot] is None)
        if is_free:
            yield slot

    def _is_collision(self, of_slot: int, slot: int) -> bool:
        slot_value = self._values[slot]
        is_collision = self._hash_func(slot_value) <= of_slot
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
        Put **value** in the hashtable.

        Pre-condition:
            - the hashtable is not full.
            - **value** does not exist in hashtable.
            - no collision resolution error.
        Post-condition:
            - the **value** was  put in the hashtable.

        """
        if len(self) >= self._capacity:
            self._put_status = self.PUT_FULL_ERR
        else:
            self._put_status = self.PUT_COLLISION_ERR

            hash_slot = self._hash_func(value)
            for slot in self._to_free_slot_stepper(hash_slot):

                if self._values[slot] == value:
                    self._put_status = self.PUT_EXISTS_ERR
                    break

                is_free = self._values[slot] is None
                if is_free:
                    self._values[slot] = value
                    self._put_status = self.PUT_OK
                    break

    def remove(self, value: str):
        """
        Remove **value** from the hashtable.

        Pre-condition:
            - **value** exists in the hashtable.
        Post-condition:
            - **value** removed from the hashtable.

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

                # offset collisions
                to_resolve_slots = (to_remove_slot,) + collision_slots
                for replace_s, by_s in zip(to_resolve_slots,
                                           to_resolve_slots[1:]):
                    self._values[replace_s] = self._values[by_s]
                self._values[to_resolve_slots[-1]] = None

                self._remove_status = self.REMOVE_OK

    # requests:
    def __len__(self):
        """Return the number of values in the hashtable."""
        return len(tuple(filter(None.__ne__, self._values)))

    def _hash_func(self, value: str) -> int:
        """Compute **value** slot"""
        bStr = value.encode()
        slot = sum(bStr) % self._capacity
        return slot

    def get_capacity(self):
        """Return hashtable capacity."""
        return self._capacity

    def is_value(self, value: str) -> bool:
        """Check if the value is in the hashtable."""
        hash_slot = self._hash_func(value)
        for slot in self._next_busy_slot_stepper(hash_slot):

            if self._values[slot] == value:
                return True

        return False

    # method statuses requests:
    def get_put_status(self) -> int:
        """Return status of last put() call:
        one of the PUT_* constants."""
        return self._put_status

    def get_remove_status(self) -> int:
        """Return status of last remove() call:
        one of the REMOVE_* constants."""
        return self._remove_status
