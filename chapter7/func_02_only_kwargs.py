# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_02_only_kwargs.py
# Time       ：2022/2/24 21:21
# Author     ：Zhong Lei
"""

def recv(maxsize, *, block):
    'Receives a message'
    pass
# recv(1024, block=True)
# recv(1023, True)


def minum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minum(1, 5, 2, -5, 10))
print(minum(1, 5, 2, -5, 10, clip=0))