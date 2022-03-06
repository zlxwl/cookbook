# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_11_simplify_init.py
# Time       ：2022/3/6 20:30
# Author     ：Zhong Lei
"""
import math
class Struct1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expect {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

class Struct2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('typing error')

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid arguments(s): {}'.format(' '.join(kwargs)))


class Stock(Struct2):
    _fields = ['name', 'shares', 'price']


class Point(Struct1):
    _fields = ['x', 'y']


import math
class Circle(Struct1):
    _fields = ['radius']
    def area(self):
        return math.pi * self.radius ** 2

s = Stock('apple', 50, 70.20)
print(s.name)
p = Point(2.0, 3.0)
print(p.x)
c = Circle(5)
print(c.area())


s1 = Stock('apple', 50, 70.20)
s2 = Stock('apple', shares=50, price=70.2)
s3 = Stock('apple', 50, price=70.2)