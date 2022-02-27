# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_06_define_lambda.py
# Time       ：2022/2/27 22:28
# Author     ：Zhong Lei
"""
add = lambda x, y: x+y
print(add(2 ,3))
print(add('hello', 'world'))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

