# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_13_data_model_check_2.py
# Time       ：2022/3/20 22:44
# Author     ：Zhong Lei
"""
class Descriptor:
    def __init__(self, name=None, **opt):
        self.name = name
        for key, value in opt.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    super_set = cls.__set__
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type))
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls


def Unsigned(cls):
    super_set = cls.__set__
    def __set__(self, instance, value):
        if value < 0 :
            raise ValueError('value must be > 0')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls


def MaxSized(cls):
    super_init = cls.__init__
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)
    cls.__init__ = __init__

    super_set = cls.__set__
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('value must < ' + str(self.size))
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls


@Typed(int)
class Integer(Descriptor):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass



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