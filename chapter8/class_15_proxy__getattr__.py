# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_15_proxy__getattr__.py
# Time       ：2022/3/21 22:24
# Author     ：Zhong Lei
"""
class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class A:
    def spam(self, x):
        print(A.__name__ + ' spam' + str(x))

    def foo(self):
        print(A.__name__ + ' foo')


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        print(B.__name__ + 'bar')

    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.bar()
b.spam(5)
b.foo()


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setting:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super(Proxy, self).__delattr__(name)
        else:
            print('deleting:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('spam.bar', self.x, y)


s = Spam(2)
p = Proxy(s)

print(p.x)
p.bar(3)
p.x = 37
