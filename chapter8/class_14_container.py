# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_14_container.py
# Time       ：2022/3/21 21:42
# Author     ：Zhong Lei
"""
from collections.abc import Sequence, Iterable
import bisect


class A(Iterable):
    pass


class SortedItems(Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return list.__str__(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(items)
print(items[0])
print(items[-1])
items.add(2)
print(items)
items.add(-10)
print(items)
print(3 in items)
print(len(items))


from collections.abc import Iterable, Sequence, Container, Sized, Mapping
print(isinstance(items, Iterable))
print(isinstance(items, Sequence))
print(isinstance(items, Container))
print(isinstance(items, Sized))
print(isinstance(items, Mapping))






