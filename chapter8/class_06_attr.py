# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_06_attr.py
# Time       ：2022/3/3 22:49
# Author     ：Zhong Lei
"""
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('can not delete')


a = Person('aa')
print(a.first_name)
a.first_name = 'bb'
print(a.first_name)


class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def set_first_name(self, first_name):
        if not isinstance(first_name, str):
            raise ValueError('first_name must be str')
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def delete_first_name(self):
        raise AttributeError('can not be delete this attr')

    name = property(set_first_name, get_first_name, delete_first_name)


p = Person('aa')
print(p.get_first_name())
p.set_first_name('bb')
print(p.get_first_name())


import math
class Circle:
    def __init__(self, radis):
        self.radis = radis

    @property
    def area(self):
        return math.pi * self.radis ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radis

a = Circle(4.0)
print(a.area)
print(a.perimeter)
