"""
----------------------- TASK 15 -----------------------

    Приведите пример небольшой иерархии, где наследование
    применяется вместо некоторого поля родительского класса
    с набором предопределённых значений.

"""
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

