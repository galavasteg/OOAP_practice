"""
----------------------- TASK 9 -----------------------

    Постройте в вашем языке программирования базовую иерархию из
    двух классов General и Any. Унаследуйте General от универсального
    базового класса, если таковой имеется в языке или стандартной
    библиотеке/фреймворке, и реализуйте семь фундаментальных операций
    для него, используя для этого по возможности возможности
    стандартных библиотек.

В Python операции:
    1) проверка типа (является ли тип текущего объекта указанным типом);
    2) получение реального типа объекта (непосредственного класса,
        экземпляром которого он был создан)
- поддерживаются встроенными функциями языка: isinstance() и
type() соответственно.

Чаще всего, обычное сравнение объектов (a == b) в Python реализовано
в глубоком варианте, стало быть покрывает операцию:
    3) сравнение объектов (включая глубокий вариант).
Однако, при реализации иерархии классов имеет смысл создавать
явный метод описывающий сравнение объектов: __eq__()

Глубокое копирование объектов можно осуществить с помощью функции
стандартной библиотеки copy.deepcopy(). Функция copy.deepcopy()
ведет себя так, как того требует операция:
    4) клонирование объекта (создание нового объекта и глубокое
        копирование в него исходного объекта).
Но, чтобы не было разночтений (deepcopy VS clone), думаю, стоит
явно определять у класса метод clone().

Остальные операции:
    3) сравнение объектов (включая глубокий вариант).
    4) клонирование объекта (создание нового объекта и глубокое
        копирование в него исходного объекта).
    6) сериализация/десериализация (перевод в формат, подходящий для
        удобного ввода-вывода, как правило в строковый тип, и
        восстановление из него);
    7) печать (наглядное представление содержимого объекта в текстовом
        формате)
реализованы ниже.

"""

from __future__ import annotations
import pickle
from copy import deepcopy
from typing import final, TypeVar


_T = TypeVar('_T')


class General(object):

    # requests:
    @final
    def __eq__(self, other: _T) -> bool:
        return self.__dict__ == other.__dict__

    @final
    def __repr__(self) -> str:
        s = f'<"{self.__class__.__name__}" instance' \
            f' (id={id(self)}): {self.__dict__}>'
        return s

    @final
    def clone(self) -> _T:
        clone = deepcopy(self)
        return clone

    @final
    def serialize(self) -> bytes:
        bs = pickle.dumps(self)
        return bs
    @final
    @classmethod
    def deserialize(cls, bs: bytes) -> _T:
        instance = pickle.loads(bs)
        return instance


class Any(General):
    """
    >>> a = Any()
    >>> isinstance(a, Any), isinstance(a, General)
    (True, True)
    >>> type(a) == Any, type(a) == General
    (True, False)

    >>> bs = a.serialize()
    >>> deser_a = Any.deserialize(bs)
    >>> a == deser_a, a is deser_a
    (True, False)

    >>> a_clone = a.clone()
    >>> a == a_clone, a is a_clone
    (True, False)

    >>> a  # doctest: +ELLIPSIS
    <"Any" instance (id=...): {'_copy_status': 0}>

    """


"""
----------------------- TASK 10 -----------------------

    Выясните, имеется ли в вашем языке программирования возможность
    запрета переопределения методов в потомках, и приведите пример кода.

Такая возможность, и для методов, и для самих классов,
появилась в Python 3.8 на уровнке type checker'а: с помощью
декоратора @final (использован в предыдущем задании).

Пример попыток переопределить final-методы/классы:

"""


class Base:
    @final
    def do_not_override_this(self) -> None: ...

class A(Base):
    # error: Cannot override final attribute "do_not_override_this"
    #  (previously declared in base class "Base")
    def do_not_override_this(self) -> None: ...


@final
class FinalBase: ...

# error: Cannot inherit from final class "FinalBase"
class B(FinalBase): ...
