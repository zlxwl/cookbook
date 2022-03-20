# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_13_data_model_check_1.py
# Time       ：2022/3/20 21:42
# Author     ：Zhong Lei
"""
class Descriptor:
    def __init__(self, name=None, **opt):
        self.name = name
        for key, value in opt.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('value must be > 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('size must be <' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Typed):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Unsigned, Float):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


## exaple1
class Stock:
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACME', 50, 91.1)
print(s.name)
print(s.shares)
print(s.price)


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


@check_attributes(name=SizedString(size=8), shares=UnsignedInteger, price=UnsignedFloat)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock('ACME', 50, 91.1)
print(s.name)
print(s.shares)
print(s.price)


class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key

        return type.__new__(cls, clsname, bases, methods)


class Stock(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock('ACME', 50, 91.1)
print(s.name)
print(s.shares)
print(s.price)





