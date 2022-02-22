# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_07_iter_slice.py
# Time       ：2022/2/22 22:09
# Author     ：Zhong Lei
"""
import itertools


def count(n):
    while True:
        yield n
        n += 1

# 迭代器和生成器无法使用切片， islice是通过丢弃前面的数据实现的，如果想要访问前面的数据需要再次生成。
c = count(0)
for number in itertools.islice(c, 10, 20):
    print(number)