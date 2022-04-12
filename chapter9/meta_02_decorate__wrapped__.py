# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_02_decorate__wrapped__.py
# Time       ：2022/4/11 22:36
# Author     ：Zhong Lei
"""
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n:int):
    '''
    count down n
    :param n: 
    :return: 
    '''
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(1000000)
    print(countdown.__annotations__)
    print(countdown.__doc__)
    print(countdown.__name__)
    print(countdown.__dict__)

    # print(countdown.__wrapped__(100000))
    from inspect import signature
    print(signature(countdown))

    origin = countdown.__wrapped__
    origin(1000000)