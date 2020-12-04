"""
----------------------- TASK 22 -----------------------

    Приведите пример иерархии, которая реализует наследование вида, и объясните, почему.

Любой товар может принадлежать разным категориям одновременно.
Более того, сами категории могут has-a другие категории.

1) Фрукты - чаще весовые товары, как, например, гвозди.
2) Котлеты могут быть мясным полуфабрикатом или готовой едой, но вегетарианские котлеты - уже не мясной продукт...

"""
from typing import Iterable, TypeVar

T_co = TypeVar('T_co', covariant=True)


class Category:
    def __init__(self, categories=Iterable['Category'], *args, **kwargs): ...

CategoryT_co = T_co[Category]


class Computers(Category): ...
class Clothes(Category): ...
class TableGames(Category): ...

class WeightGoods(Category): ...

class Food(Category): ...
class Fish(Food): ...
class Meat(Food): ...
class Vegetables(Food): ...

class Good:
    def __init__(self, categories: Iterable[CategoryT_co], **attributes):
        self.categories = tuple(categories)
        known_attrs = ...  # dynamically collect all allowed attributes by categories
        for attr in known_attrs:
            setattr(self, attr, attributes.get(attr))


cucumber = Good(categories=[Vegetables, WeightGoods])
