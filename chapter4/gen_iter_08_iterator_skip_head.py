# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_08_iterator_skip_head.py
# Time       ：2022/2/22 22:14
# Author     ：Zhong Lei
"""
from itertools import dropwhile


with open('pwd', encoding='utf-8', errors='ignore') as f:
    for line in dropwhile(lambda line: str(line).startswith('#'), f):
        print(line, end='')


# 知道需要跳过的元素位置
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

def count(n):
    while n>0:
        yield n
        n -= 1
c = count(10)

for number in islice(c, 3, None):
    print(number)


# 如果不使用islice 或者dropwhile
with open('pwd') as f:
    while True:
        line = next(f)
        if not line.startswith('#'):
            break

    while line:
        print(line, end='')
        line = next(f, None)


# 过滤
with open('pwd', 'r', encoding='utf-8', errors='ignore') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

