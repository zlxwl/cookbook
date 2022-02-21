# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_03_generator.py
# Time       ：2022/2/21 22:26
# Author     ：Zhong Lei
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for x in frange(0, 4, 0.5):
    print(x)

print(list(frange(0, 1, 0.125)))


# 生成器只在响应迭代的时候才会运行。
def count_down(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = count_down(3)
print(next(c))
print(next(c))
print(next(c))


