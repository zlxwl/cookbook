# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_14_yield_from_nested_sequence.py
# Time       ：2022/2/23 21:38
# Author     ：Zhong Lei
"""
item = [1, 2, [3, 4, [5, 6], 7], 8]

from collections import Iterable

def flatten(items, ignore_types = (bytes, str)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

for x in flatten(item):
    print(x)

items = ['Dave', 'Paule', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)


def flatten(items, ignore_types = (bytes, str)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
            # yield from flatten(x)
        else:
            yield x
for x in flatten(items):
    print(x)
