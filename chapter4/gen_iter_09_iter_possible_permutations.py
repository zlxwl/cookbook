# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_09_iter_possible_permutations.py
# Time       ：2022/2/23 20:36
# Author     ：Zhong Lei
"""

# 排列
items = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(items):
    print(p)
for p in permutations(items, 2):
    print(2)

# 组合
from itertools import combinations
for p in combinations(items, 3):
    print(p)
for p in combinations(items, 2):
    print(p)
for p in combinations(items, 1):
    print(p)

from itertools import combinations_with_replacement
for p in combinations_with_replacement(items, 3):
    print(p)
for p in combinations_with_replacement(items, 2):
    print(p)

