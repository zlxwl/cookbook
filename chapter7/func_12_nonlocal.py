# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_12_nonlocal.py
# Time       ：2022/3/1 23:08
# Author     ：Zhong Lei
"""

def sample():
    n = 0

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value
        return n

    def func():
        print('n=', n)

    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()

f.set_n(10)
f()

print(f.get_n())