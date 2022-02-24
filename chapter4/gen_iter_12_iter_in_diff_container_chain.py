# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_12_iter_in_diff_container_chain.py
# Time       ：2022/2/23 21:22
# Author     ：Zhong Lei
"""
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

# active_items = set()
# inactive_items = set()
# for x in chain(active_items, inactive_items):
#     print(x)