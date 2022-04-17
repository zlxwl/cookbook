# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_06_decorate_partial.py
# Time       ：2022/4/16 13:58
# Author     ：Zhong Lei
"""
from functools import partial, wraps
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    log_name = name if name else func.__module__
    log = logging.getLogger(log_name)
    log_message = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, log_message)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(x, y):
    return x + y


@logged(level=logging.WARN, name='countdown', message='countdown_function')
def countdown(n):
    while n>0:
        n -= 1


if __name__ == '__main__':
    add(2, 3)
    countdown(20)