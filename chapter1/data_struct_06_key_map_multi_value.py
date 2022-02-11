# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_06_key_map_multi_value.py
# Time       ：2022/2/11 22:55
# Author     ：Zhong Lei
"""
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(3)
print(d)

f = defaultdict(set)
f['a'].add(1)
f['b'].add(2)
f['c'].add(3)
print(f)


# 初始化的最优写法
d = defaultdict(list)
pairs = {'a': 3, 'b': 5}
for key, value in pairs:
    d[key].append(value)

# 不好的写法
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    else:
        d[key].append(value)