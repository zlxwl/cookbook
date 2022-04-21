# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_20_types_descriptor_v2.py
# Time       ：2022/4/21 22:46
# Author     ：Zhong Lei
"""
import types


class multimethod:
    def __init__(self, func):
        self._methods = {}

        self.__name__ = __name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults + 1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class Spam:
    @multimethod
    def bar(self, *args):
        raise TypeError('no matching method for bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print('bar1 :', x, y)

    # @bar.match(str, int)
    # def bar(self, s, n=0):
    #     print('bar2 :', s, n)


if __name__ == '__main__':
    a = Spam()

    a.bar(1, 2)
    # a.bar('hello', 2)