"""
----------------------- TASK 15 -----------------------

    Приведите пример небольшой иерархии, где наследование
    применяется вместо некоторого поля родительского класса
    с набором предопределённых значений.

"""
import warnings
from typing import Any as t_Any, Tuple

from part_2_OOP.tasks11_13_closure_privates_assignment_attempt import Any


class _ClassificationDataInput(Any):
    """ADT for classification inputs."""
    def get_prepared(self, *args, **kwargs) -> t_Any:
        """Request method, must return acceptable
        object as input for classification model."""
        raise NotImplementedError()


class YesNoQuestionnaire(_ClassificationDataInput):
    """
    >>> q = YesNoQuestionnaire()
    >>> q.get_prepared(True, False, True)
    (1, 0, 1)

    """
    def get_prepared(self, *user_answers: bool, **kwargs) -> Tuple[int, ...]:
        prepared = tuple(map(int, user_answers))
        return prepared


class MovementTest(_ClassificationDataInput):
    """
    >>> BAD, AVERAGE, GOOD = range(3)
    >>> m = MovementTest()
    >>> m.get_prepared(BAD, GOOD, AVERAGE)
    (0, 2, 1)

    """
    def get_prepared(self, *test_result_enums: int, **kwargs) -> Tuple[int, ...]:
        prepared = test_result_enums
        return prepared


"""
----------------------- TASK 16 -----------------------

    Если используемый вами язык программирования это допускает,
    напишите примеры полиморфного и ковариантного вызовов метода.

В Python, используя иерархию классов выше, можно показать ковариантный 
и полиморфный вызов метода Preprocessor.get_prepared_data(),
принимающий пары экземпляров-потомков _ClassificationDataInput и их 
входные данные: [(T(), data), ...]

Ковариантность выражается в первом объекте пары, второй объект - 
полиморфный(е) аргумент(ы) для метода get_prepared(...) первого объекта.

При таком возове метода Preprocessor.get_prepared_data()
возникает ограничение на контракт вызова get_prepared().
Программист вынужден это помнить при создании нового потомка
класса _ClassificationDataInput.

"""

UserData = Tuple[Tuple[_ClassificationDataInput, t_Any], ...]
InputData = Tuple[Tuple[int, ...], ...]


class Preprocessor(Any):
    """Model input preprocessor

    >>> BAD, AVERAGE, GOOD = range(3)
    >>> user_data_to_classify = (
    ...     (YesNoQuestionnaire(), (True, False, True, True)),
    ...     (MovementTest(), (GOOD, GOOD, BAD, AVERAGE)),
    ... )
    >>> p = Preprocessor()
    >>> p.get_prepared_data(user_data_to_classify)
    ((1, 0, 1, 1), (2, 2, 0, 1))
    """

    def get_prepared_data(self, user_data_to_classify: UserData) -> InputData:
        warnings.warn(
            'Строгое решение запрещает использовать некую сущность'
            ' в программе одновременно и как полиморфную, и как ковариантную.',
            DeprecationWarning)
        input_data = tuple(input_inst.get_prepared(*data)
                           for input_inst, data in user_data_to_classify)
        return input_data
