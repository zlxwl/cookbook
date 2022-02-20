# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_20_merge_dict.py
# Time       ：2022/2/20 21:38
# Author     ：Zhong Lei
"""
a = {'x': 1, 'y': 3}
b = {'y': 2, 'z': 4}


from collections import ChainMap
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['z'])
print(c['y'])
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']
print(c)
print(a)
print(b)
