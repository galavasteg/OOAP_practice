"""
----------------------- TASK 7 -----------------------

    Приведите пример кода с комментариями, где применяется
    динамическое связывание.

Методы в Python виртуальные по умолчанию,
что дает возможность осуществлять позднее связывание
достаточно легко с помощью переопределения метода предка:
>>> class Animal:
...     def eat(self):
...         print('Animal is eating')
>>> class Dog(Animal):
...     # I override the method eat() of class Animal.
...     # This uses dynamic binding
...     def eat(self):
...         print('Dog is eating')
>>> dog = Dog()
>>> dog.eat()  # dynamic binding: Python defines which method to call
Dog is eating
>>> Animal.eat(dog)  # static binding: I say: "use Animal class method for eating"
Animal is eating

"""

