# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_11_zip.py
# Time       ：2022/2/23 21:09
# Author     ：Zhong Lei
"""

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

# zip是最短
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for x, y in zip(a, b):
    print(x, y)

# ziplongest
from itertools import zip_longest
for x, y in zip_longest(a, b, fillvalue=0):
    print(x, y)


# zip创建字典
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)