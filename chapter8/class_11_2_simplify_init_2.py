# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_11_2_simplify_init_2.py
# Time       ：2022/3/6 21:00
# Author     ：Zhong Lei
"""

class Struct3:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expect {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicated values for {}'.format(','.join(kwargs)))


class Stock(Struct3):
    _fields = ['apple', 'shares', 'price']


if __name__ == '__main__':
    s1 = Stock('apple', 70, 70.1)
    s2 = Stock('apple', 90, 79, data='20220306')
    s3 = Stock('apple', 90, 88, data='20220306')
    print(s3.__dict__['data'])
