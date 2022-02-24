# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_03_value_type_hint.py
# Time       ：2022/2/24 21:32
# Author     ：Zhong Lei
"""

def add(x: int, y: int) -> int:
    return x+y
print(add(3, 4))

print(help(add))
print(add.__annotations__)


