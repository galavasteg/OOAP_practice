"""
Task 1.
Write a small code example with comments where
inheritance, composition, and polymorphism are applied.

Task 2.
Write a small code example with comments where
inheritance applies both the extension of the parent class
and the specialization of the parent class.

Task 3.
Explain how the "class as a module" concept is supported
in Python.

"""


# -------------------- Task 1 -----------------------
# Write a small code example with comments where
# inheritance, composition, and polymorphism are applied.

class Wheel:
    def __init__(self):
        print('wheel...')


# Composition: Bicycle "has-a" wheel(s)
class Bicycle:
    """
    >>> b = Bicycle()
    wheel...
    wheel...
    """
    def __init__(self, wheel_count: int = 2):
        self.wheels = [Wheel() for _ in range(wheel_count)]


# Inheritance <==> "is-a"
# Polymorphism: Bike "is-a" Bicycle with 2 wheels
class Bike(Bicycle):
    """
    >>> bike = Bike()
    wheel...
    wheel...
    """
    def __init__(self):
        super().__init__(wheel_count=2)


# -------------------- Task 2 -----------------------
# Write a small code example with comments where
# inheritance applies both the extension of the parent class
# and the specialization of the parent class.

class Engine:
    def __init__(self, power: float):
        self.power = power
        print('engine power is', power)


# Specialization: road bicycles are a subset of bicycles
# Extension: bicycle extended by an engine
class ElectricRoadBicycle(Bicycle):
    """
    >>> m = ElectricRoadBicycle(power=20.5)
    wheel...
    wheel...
    engine power is 20.5
    I can a-ron-don-don!
    """
    def __init__(self, power: float):
        super().__init__()

        self.engine = Engine(power)

        print('I can a-ron-don-don!')


# -------------------- Task 3 -----------------------
# Explain how the "class as a module" concept is supported
# in Python.

"""
There are huge differences between classes and modules in Python.

Classes are blueprints that allow you to create instances with
attributes and bound functionality. Classes support inheritance,
metaclasses, and descriptors.

Modules can't do any of this, modules are essentially singleton
instances of an internal module class, and all their globals are
attributes on the module instance. You can manipulate those attributes
as needed (add, remove and update), but take into account that these
still form the global namespace for all code defined in that module.

Modules can contain more than just one class however; functions
and any the result of any other Python expression can be globals
in a module too.

So as a general ballpark guideline:
    Use classes as blueprints for objects that model your problem domain.
    Use modules to collect functionality into logical units.

Global state goes in modules (and functions and classes are just as much
global state, loaded at the start). Everything else goes into other data
structures, including instances of classes.

"""
