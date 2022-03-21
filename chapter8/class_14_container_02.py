# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_14_container_02.py
# Time       ：2022/3/21 22:14
# Author     ：Zhong Lei
"""
from collections.abc import MutableSequence
import bisect


class Items(MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, index):
        print('getting {}'.format(index))
        return self._items[index]

    def __setitem__(self, key, value):
        print('setting {} to {}'.format(key, value))
        self._items[key] = value

    def __delitem__(self, key):
        print('deleting {}'.format(key))
        del self._items[key]

    def insert(self, index, value):
        print('inserting {}: {}'.format(index, value))
        self._items.insert(index, value)

    def __len__(self):
        print('len')
        return len(self._items)

    def __str__(self):
        return list.__str__(self._items)


a = Items([1, 2, 3])
print(len(a))

a.append(4)

print(a.count(2))

print(a.remove(2))
