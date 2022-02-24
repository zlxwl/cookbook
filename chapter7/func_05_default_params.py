# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_05_default_params.py
# Time       ：2022/2/24 21:42
# Author     ：Zhong Lei
"""

def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)

# 默认参数是可变对象， list，dict，set，使用None作为默认值。
def spam(a, b=None):
    if b is None:
        b = []

_no_value = object()
def spam(a, b = _no_value):
    if b is _no_value:
        print('No b value supplied')

x = 42
def spam(a, b=x):
    print(a, b)
spam(1)
x = 23
spam(1)


