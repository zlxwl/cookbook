# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_05_decorate_attach_wrapper.py
# Time       ：2022/4/12 19:46
# Author     ：Zhong Lei
"""
from functools import wraps, partial
import logging
import sys
sys.path.append('.')
from chapter9.meta_02_decorate__wrapped__ import timethis


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmessage = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmessage)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal logmessage
            logmessage = new_message

        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('spam !')


@logged(logging.DEBUG)
@timethis
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    import logging
    # logging.basicConfig(level=logging.DEBUG)
    # print(add(2, 3))
    #
    # add.set_message('Add called')
    # print(add(2, 3))
    #
    # add.set_level(logging.WARN)
    # print(add(2, 3))

    countdown(1000000)

    countdown.set_message('count down to zero')
    countdown.set_level(logging.WARNING)
    countdown(1000000)