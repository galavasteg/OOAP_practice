"""
Task 1.
Write a small code example with comments where
inheritance, composition, and polymorphism are applied.

Task 2.
Write a small code example with comments where
inheritance applies both the extension of the parent class
and the specialization of the parent class.

"""


# -------------------- Task 1 -----------------------
# Write a small code example with comments where
# inheritance, composition, and polymorphism are applied.

class HasWheels:
    def __init__(self, w_count: int):
        self.wheel_count = w_count
        print('I have %s wheels' % w_count)


# Composition: Bicycle "has-a" wheel(s)
class Bicycle:
    """
    >>> b = Bicycle()
    I have 2 wheels
    """
    def __init__(self, wheels: int = 2):
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


# -------------------- Task 2 -----------------------
# Write a small code example with comments where
# inheritance applies both the extension of the parent class
# and the specialization of the parent class.

class HasEngine:
    def __init__(self, power: float):
        self.power = power
        print('My power is', power)


# Inheritance: Motorcycle "is-a" Bicycle with one
#              wheel and with an engine
class MotoMonocycle(Bicycle):
    """
    >>> m = MotoMonocycle(power=20.5)
    I have 1 wheels
    My power is 20.5
    I can a-ron-don-don!
    """
    def __init__(self, power: float):
        # Specialization: monocycles are a subset of bicycles
        super().__init__(wheels=1)

        # Extension: MotoMonocycle extends Bicycle with an engine
        self.engine = HasEngine(power)

        print('I can a-ron-don-don!')

