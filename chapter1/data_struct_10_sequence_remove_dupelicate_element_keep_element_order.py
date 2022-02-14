# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_10_sequence_remove_dupelicate_element_keep_element_order.py
# Time       ：2022/2/13 22:35
# Author     ：Zhong Lei
"""
# 序列中的元素是可哈希的才能这么做
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

# 序列中的元素不可哈希, key指定一个函数，用来将序列中的元素类型转换为可哈希的。
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)

a = [{'x': 1, 'y':2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))


