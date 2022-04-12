# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_01_functools_wraps.py
# Time       ：2022/4/11 22:07
# Author     ：Zhong Lei
"""
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        last = time.time() - start
        print(func.__name__, last)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    countdown(1000000)