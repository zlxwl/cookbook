# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_04_decorate_params.py
# Time       ：2022/4/11 22:55
# Author     ：Zhong Lei
"""
from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    data = add(10, 12)
    spam()