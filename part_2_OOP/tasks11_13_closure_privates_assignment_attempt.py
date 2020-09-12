"""
----------------------- TASK 11 -----------------------

    Если используемый вами язык программирования допускает множественное
    наследование, постройте небольшую иерархию, используя уже готовые General
    и Any, и замкните её снизу классом None. Приведите пример полиморфного
    использования Void.

Ниже, с помощью класса `VoidType`, замкнута небольшая иерархия.
Полиморфное использование Void в задании 12 в классе `Knight` в 2х местах:
    1. команда hit(target) проверяет "пустотность" параметра target
       с помощью ключевого слова 'if' с неявным приведением None -> False
    1. запрос get_dmg() проверяет у оружия наличие атрибута 'damage',
       который добавлен не был, с помощью ключевого слова
       'getattr' cо значением по-умолчанию, используемое в случае
       отсутствия атрибута.

"""
from typing import Optional

from part_2_OOP.tasks7_8_bindings_covariance_contravariance import (
        Sword, Broadsword, Cutlass, Shuriken)
from part_2_OOP.tasks9_10_general_class_hierarchy import Any, General

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


class CutlassHierarchyBottom(Cutlass_, VoidType):
    """
    >>> c = CutlassHierarchyBottom()
    >>> c.serialize()
    Traceback (most recent call last):
        ...
    AttributeError: 'NoneType' object has no attribute 'serialize'
    >>> class TryInheritFromClosedHierarchy(CutlassHierarchyBottom, Any): ...
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


class Unit(Any):
    def take_damage(self, dmg: int):
        print(f'{type(self).__name__} took {dmg=}')
class Orc(Unit): ...
class Knight(Unit):
    """
    >>> sword = Sword_()
    >>> unit = Knight(sword)
    >>> unit.weapon  # doctest: +ELLIPSIS
    <"Sword_" instance (id=...): {'_copy_status': 0, '_assignment_status': 0}>

    >>> compatible_weapon = Broadsword_()
    >>> unit.assignment_attempt('weapon', compatible_weapon)
    >>> unit.weapon  # doctest: +ELLIPSIS
    <"Broadsword_" instance (id=...): {'_copy_status': 0, '_assignment_status': 0}>
    >>> unit.get_assignment_attempt_status() == sword.ASSIGNMENT_OK
    True

    >>> incompatible_weapon = Shuriken_()
    >>> unit.assignment_attempt('weapon', incompatible_weapon)
    >>> unit.get_assignment_attempt_status() == unit.ASSIGNMENT_INCOMPATIBLE
    True
    >>> type(unit.weapon) == Void
    True

    """

    def __init__(self, weapon: Any,
                 *args, **kwargs):
        super().__init__(weapon, *args, **kwargs)
        self.weapon = weapon
        self.attack_dmg = 12

    def get_damage(self) -> int:
        dmg = self.attack_dmg + getattr(self.weapon, 'damage', 0)
        return dmg

    def hit(self, target: Optional[Unit] = void) -> None:
        """
        >>> knight = Knight(Sword_())
        >>> target_unit = Orc()
        >>> knight.hit(target_unit)
        Orc took dmg=12

        """
        if not target:
            return

        target.take_damage(self.get_damage())


"""
----------------------- TASK 13 -----------------------

    Разберитесь, какие из четырёх вариантов скрытия методов:
    1. метод публичен в родительском классе А и публичен в его потомке B;
    2. метод публичен в родительском классе А и скрыт в его потомке B;
    3. метод скрыт в родительском классе А и публичен в его потомке B;
    4. метод скрыт в родительском классе А и скрыт в его потомке B.
    - доступны в используемом вами языке программирования. Приведите
    примеры кода для каждого из доступных вариантов.

В Python поддерживается вариант 1 в полной мере, примеры можно найти в
иерархиях классов предыдущих заданий.
Остальные варианты, т.к. в языке нет по-настоящему скрытых методов, -
с оговорками:
    1. принято "строгое сокрытие" помечать двумя подчеркиваниями '__'
       перед именем атрибута/метода. Не могу сказать что это удобно,
       т.к. усложняет тестирование.
    2. "нестрогое сокрытие" - помечать одним подчеркиванием '_'. В
       целом, это правило является разумным компромиссом между
       - удобством командной разработки,
       - применением возможностей тайпчекера
       - и простоты тестирования

Запрета использования "скрываемых" атрибутов можно добиться с помощью
исключений:
"""

# 2: метод публичен в родительском классе А и скрыт в его потомке B
class A2:
    def m(self):
        """
        >>> a = A2()
        >>> a.m()
        """
class B2(A2):
    def m(self):
        """
        >>> b = B2()
        >>> b.m()
        Traceback (most recent call last):
        ...
        AttributeError
        """
        raise AttributeError

# 3: метод скрыт в родительском классе А и публичен в его потомке B
class A3:
    def m(self):
        """
        >>> a = A3()
        >>> a.m()
        Traceback (most recent call last):
        ...
        NotImplementedError
        """
        raise NotImplementedError
class B3(A3):
    def m(self):
        """
        >>> b = B3()
        >>> b.m()
        """

# 4: метод скрыт в родительском классе А и скрыт в его потомке B
class A4:
    def __m(self):
        """
        >>> a = A4()
        >>> a.__m()
        Traceback (most recent call last):
        ...
        AttributeError: 'A4' object has no attribute '__m'

        >>> a._A4__m()  # but this works fine
        """
class B4(A4):
    """
    >>> b = B4()
    >>> b.__m()
    Traceback (most recent call last):
    ...
    AttributeError: 'B4' object has no attribute '__m'

    >>> b._A4__m()  # but this works fine
    """
