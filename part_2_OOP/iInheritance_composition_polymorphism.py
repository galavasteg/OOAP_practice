"""
Task 1.
Write a small code example with comments where
inheritance, composition, and polymorphism are applied.

"""


# -------------------- Task 1 -----------------------

class HasWheels:
    def __init__(self, w_count: int):
        self.wheel_count = w_count
        print('I have %s wheels' % w_count)


class HasEngine:
    def __init__(self, power: float):
        self.power = power
        print('My power is', power)


class Bicycle:
    """
    >>> b = Bicycle()
    I have 2 wheels
    """
    def __init__(self, wheels: int = 2):
        # Composition: Bicycle "has-a" wheel(s)
        self.wheels = HasWheels(wheels)


# Inheritance <==> "is-a"
# Polymorphism: Monocycle "is-a" Bicycle with one wheel
class Monocycle(Bicycle):
    """
    >>> mono = Monocycle()
    I have 1 wheels
    """
    def __init__(self):
        super().__init__(wheels=1)


# Inheritance: Motorcycle "is-a" Bicycle with an engine
class Motorcycle(Bicycle):
    """
    >>> m = Motorcycle(wheel_count=2, power=20.5)
    I have 2 wheels
    My power is 20.5
    I can a-ron-don-don!
    """
    def __init__(self, wheel_count: int, power: float):
        # Call Bicycle (parent) __init__ implementation
        super().__init__(wheel_count)

        # Composition: Motorcycle "has-an" engine
        self.engine = HasEngine(power)

        # Motorcycle-class __init__ implementation:
        print('I can a-ron-don-don!')
