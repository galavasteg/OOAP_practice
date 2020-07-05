"""
----------------------- TASK 7 -----------------------

    Приведите пример кода с комментариями, где применяется
    динамическое связывание.

Методы в Python виртуальные по умолчанию,
что дает возможность осуществлять позднее связывание
достаточно легко с помощью переопределения метода предка:
>>> class Animal:
...     def eat(self):
...         print('Animal is eating')
>>> class Dog(Animal):
...     # I override the method eat() of class Animal.
...     # This uses dynamic binding
...     def eat(self):
...         print('Dog is eating')
>>> dog = Dog()
>>> dog.eat()  # dynamic binding: Python defines which method to call
Dog is eating
>>> Animal.eat(dog)  # static binding
Animal is eating


----------------------- TASK 8 -----------------------

    Приведите примеры кода с ковариантностью и контравариантностью,
    если ваш язык программирования это позволяет.

Предыдущая строчка кода демонстрирует и ковариантную типизацию:
метод предка Animal.eat() принимает на вход экземпляр
потомка Dog.

Другая схема ковариантности.
Переопределённый метод get_melee_weapon() возвращает
значение типа (FuryBlade), являющимся потомком типа (Sword),
возвращаемого родительским методом.
>>> class Sword: ...
>>> class FuryBlade(Sword): ...
>>> class Knight:
...     def get_melee_weapon(self):
...         return Sword()
>>> class Paladin(Knight):
...     def get_melee_weapon(self):
...         return FuryBlade()
...
>>> knigt, paladin = Knight(), Paladin()
>>> s, fb = knigt.get_melee_weapon(), paladin.get_melee_weapon()
>>> isinstance(s, Sword), isinstance(s, FuryBlade)
(True, False)
>>> isinstance(fb, Sword), isinstance(fb, FuryBlade)
(True, True)

Интересно, что в Python есть возможность создавать свои
generic types с явным указанием ковариантости или
контравариантности типов (по-умолчанию, инвариантны).

Сам интерпретатор их проигнорирует. Однако, настроив
статический анализатор кода, например MyPy, можно
повысить надежность кода.

Контравариантность можно продемонстрировать следующим
примером, где sharpen_melee_weapon - делегат, параметризованный
самым "глубоким" потомком одной из веток оружия.
MyPy - статический анализатор - типы других веток и потомков
Broadsword "не пропустит".

"""

from typing import TypeVar, Generic

T_contra = TypeVar('T_contra', contravariant=True)

class _T(Generic[T_contra]):
    def __init__(self, item: T_contra) -> None: ...


class BladedWeapon: ...

class Sword(BladedWeapon): ...
class Broadsword(Sword): ...
class Cutlass(Broadsword): ...

class Shuriken(BladedWeapon): ...


def sharpen_melee_weapon(weapon: _T[Broadsword]) -> None: ...


sword1, sword2 = _T(Broadsword()), _T(Sword())
sharpen_melee_weapon(sword1)  # OK
sharpen_melee_weapon(sword2)  # OK, "Sword" is an ancestor of "Broadsword"

shuriken = _T(Shuriken())
# error: Argument 1 to "sharpen_melee_weapon" has incompatible type
#  "_T[Shuriken]"; expected "_T[Broadsword]"
sharpen_melee_weapon(shuriken)  # FAIL: another weapon branch

cutlass = _T(Cutlass())
# error: Argument 1 to "sharpen_melee_weapon" has incompatible type
#  "_T[Cutlass]"; expected "_T[Broadsword]"
sharpen_melee_weapon(cutlass)  # FAIL, "Cutlass" is a descendant of "Broadsword"
