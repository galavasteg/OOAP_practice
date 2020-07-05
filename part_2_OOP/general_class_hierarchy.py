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
