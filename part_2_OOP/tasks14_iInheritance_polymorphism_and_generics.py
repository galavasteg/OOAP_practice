"""
----------------------- TASK 14 -----------------------

    Сформируйте тип (класс) Vector<T> (линейный массив значений типа T,
    наследуемого от General), над которым допустима операция сложения,
    реализуемая как сложение соответствующих значений типа T двух векторов
    одинаковой длины. Если длины векторов различны, возвращайте Void/null
    в качестве результата работы операции сложения.
    Проверьте, насколько корректно будет работать сложение объектов типа
    Vector<Vector<Vector<T>>>.

    Выясните, как в используемом вами языке программирования элегантнее
    всего реализовать поддержку сложения элементов произвольных типов.

В Python у объектов есть возможность определить магический метод __add__,
отвечающий за поведения оператора '+' (в стандартной библиотеке
operator.add). Также в стандартной библиотеке присутствуют модули
itertools и functools, дающие возможность писать достаточно декларативные
конструкции. Одна из таких реализована ниже, в методе Vector._sum_vectors_2.

"""
import operator
from itertools import starmap
from typing import Optional, Any as t_Any

from part_2_OOP.tasks11_13_closure_privates_assignment_attempt import Void
from part_2_OOP.tasks9_10_general_class_hierarchy import General, Any


# WARNING: it is not a good way for a real project !!!
#  There must be exactly one `General` type
#  and exactly one `Any` type
class General(General):
    ...

class Any(General, Any):

    def __add__(self, other):
        """Summation"""
        raise NotImplementedError()


class Vector(Any):
    """
    >>> v1 = Vector(0, 1, 2)
    >>> v2 = Vector(7, 10, 15)
    >>> (v1 + v2).get_sequence_representation()
    (7, 11, 17)

    >>> v3 = Vector(3)
    >>> (v1 + v3) is Void
    True
    >>> v4 = Vector(6)

    >>> nested_v1 = Vector(Vector(v1), Vector(v3))
    >>> nested_v2 = Vector(Vector(v2), Vector(v4))
    >>> nested_v1.get_sequence_representation()
    (((0, 1, 2),), ((3,),))
    >>> nested_v2.get_sequence_representation()
    (((7, 10, 15),), ((6,),))
    >>> (nested_v1 + nested_v2).get_sequence_representation()
    (((7, 11, 17),), ((9,),))

    """

    def __init__(self, *args: t_Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.sequence = args
        self._size = len(args)

    def __add__(self, other: 'Vector') -> Optional['Vector']:
        try:
            assert self._size == other._size
        except AssertionError:
            sum_vector = Void
        else:

            sum_vector = self._sum_vectors(other)
        return sum_vector

    def _sum_vectors(self, other: 'Vector') -> 'Vector':
        """Vectors summation in imperative way"""
        sum_sequence = []
        for item_1, item_2 in zip(self.sequence, other.sequence):
            items_sum = item_1 + item_2
            sum_sequence.append(items_sum)

        sum_vector = Vector(*sum_sequence)
        return sum_vector

    def _sum_vectors_2(self, other: 'Vector') -> 'Vector':
        """Vectors summation in declarative style"""
        sequence_items = starmap(operator.add, zip(self.sequence, other.sequence))
        sum_vector = Vector(*sequence_items)
        return sum_vector

    def get_sequence_representation(self) -> tuple:
        """Get representation of all nested sequence (recursive)"""
        this_func_name = self.get_sequence_representation.__name__
        representation = tuple(
                getattr(item, this_func_name, lambda: item)()
                for item in self.sequence)
        return representation
