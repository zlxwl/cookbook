# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_09_dict_find_common.py
# Time       ：2022/2/12 22:23
# Author     ：Zhong Lei
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

#  element in a and b
print(a.keys() & b.keys())
#  element in a not in b
print(a.keys() - b.keys())

print(a.items() & b.items())

c = {key: a[key] for key in a.keys() - {'a', 'z'}}
print(c)
