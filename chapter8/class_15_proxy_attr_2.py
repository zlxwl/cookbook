# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_15_proxy_attr_2.py
# Time       ：2022/3/21 23:05
# Author     ：Zhong Lei
"""
class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.spam(5)
b.foo()
b.bar()


class LikeList:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __delitem__(self, key):
        del self._items[key]


likeList = LikeList()
likeList.append(2)
likeList.insert(1, 1)
print(len(likeList))
print(likeList[-1])