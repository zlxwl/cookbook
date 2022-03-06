# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_09_creat_class_or_instance_attr.py
# Time       ：2022/3/6 17:45
# Author     ：Zhong Lei
"""
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('expected int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        # x = Integer('x')
        # y = Integer('y')
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
print(p.y)


# 和装饰器一起使用
class Typed:
    def __init__(self, name, expect_type):
        self.name = name
        self.expect_type = expect_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expect_type):
            raise TypeError('expected {}'.format(self.expect_type))
        else:
            instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeasstert(**kwargs):
    def decorate(cls):
        for name, expected_value in kwargs.items():
            setattr(cls, name, Typed(name, expected_value))
        return cls
    return decorate


@typeasstert(name=str, share=int, price=float)
class Stock:
    def __init__(self, name, share, price):
        self.name = name
        self.share = share
        self.price = price

s = Stock('apple', 50, 79.00)
print(s.name)
print(s.share)
print(s.price)
