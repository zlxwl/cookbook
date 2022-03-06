# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_10_lazy_caculate.py
# Time       ：2022/3/6 19:26
# Author     ：Zhong Lei
"""
class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            # instance.__dict__[self.func.__name__] = value
            return value


def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi * self.radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2

c = Circle(4.0)
print(vars(c))
print(c.perimeter)
print(vars(c))
print(c.area)
print(vars(c))
print(c.perimeter)
print(c.area)


