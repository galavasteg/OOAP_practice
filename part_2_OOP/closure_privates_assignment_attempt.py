"""
----------------------- TASK 11 -----------------------

    Если используемый вами язык программирования допускает множественное
    наследование, постройте небольшую иерархию, используя уже готовые General
    и Any, и замкните её снизу классом None. Приведите пример полиморфного
    использования Void.

Ниже, с помощью класса `VoidType`, замкнута небольшая иерархия.
"""
from part_2_OOP.bindings_covariance_contravariance import (
        Sword, Broadsword, Cutlass, Shuriken)
from part_2_OOP.general_class_hierarchy import Any, General

# Aliases for Python `NoneType` and its instance
void = None
Void = type(None)


class VoidType:
    def __new__(self, *args, **kwargs):
        return void


class Cutlass_(Cutlass, Any):
    """
    >>> c = Cutlass_()
    >>> c.serialize()  # doctest: +ELLIPSIS
    b'...'
    """


class CutlassHierarchy(Cutlass_, VoidType):
    """
    >>> c = CutlassHierarchy()
    >>> c.serialize()
    Traceback (most recent call last):
        ...
    AttributeError: 'NoneType' object has no attribute 'serialize'
    >>> class TryInheritFromClosedHierarchy(CutlassClosed, Any): ...
    >>> TryInheritFromClosedHierarchy() == void
    True
    """


"""
----------------------- TASK 12 -----------------------

    Добавьте в классы General и Any попытку присваивания и её реализацию.

Ниже реализованы:
    1. базовые классы `General...` и `Any...` c командой `assignment_attempt`,
    2. иерархия оружия из предыдущих заданий с помощью множественного наследования.
    3. класс боевой единицы и тесты попыток сменить оружение разного типа

"""

# WARNING: it is not a good way for a real project !!!
#  There must be exactly one `General` type
#  and exactly one `Any` type
class General(General):

    ASSIGNMENT_NIL = 0
    ASSIGNMENT_OK = 1
    ASSIGNMENT_INCOMPATIBLE = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._assignment_status = self.ASSIGNMENT_NIL

    def assignment_attempt(self, target_name: str, source) -> None:
        target_type = type(getattr(self, target_name))
        if isinstance(source, target_type):
            setattr(self, target_name, source)
            self._assignment_status = self.ASSIGNMENT_OK
        else:
            setattr(self, target_name, Void())
            self._assignment_status = self.ASSIGNMENT_INCOMPATIBLE

    def get_assignment_attempt_status(self) -> int:
        """Return status of last assignment_attempt() call:
        one of the ASSIGNMENT* constants."""
        return self._assignment_status

class Any(General, Any): ...


# Two weapon branches:
class Sword_(Sword, Any): ...
class Broadsword_(Broadsword, Sword_): ...

class Shuriken_(Shuriken, Any): ...


class Knight(Any):
    """
    >>> sword = Sword_()
    >>> unit = Knight(sword)
    >>> unit.sword  # doctest: +ELLIPSIS
    <"Sword_" instance (id=...): {'_copy_status': 0, '_assignment_status': 0}>

    >>> compatible_weapon = Broadsword_()
    >>> unit.assignment_attempt('sword', compatible_weapon)
    >>> unit.sword  # doctest: +ELLIPSIS
    <"Broadsword_" instance (id=...): {'_copy_status': 0, '_assignment_status': 0}>
    >>> unit.get_assignment_attempt_status() == sword.ASSIGNMENT_OK
    True
    >>> type(unit.sword).__name__
    'Broadsword_'

    >>> incompatible_weapon = Shuriken_()
    >>> unit.assignment_attempt('sword', incompatible_weapon)
    >>> unit.get_assignment_attempt_status() == sword.ASSIGNMENT_INCOMPATIBLE
    True
    >>> type(unit.sword) == Void
    True

    """

    def __init__(self, weapon: Any,
                 *args, **kwargs):
        super().__init__(weapon, *args, **kwargs)
        self.sword = weapon
