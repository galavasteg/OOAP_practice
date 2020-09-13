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

"""
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

