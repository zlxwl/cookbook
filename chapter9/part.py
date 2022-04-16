# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : part.py
# Time       ：2022/4/15 22:26
# Author     ：Zhong Lei
"""
from functools import partial, wraps
import logging
import time


def f(obj, func=None):
    if func is None:
        return partial(f, obj)
    return func


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    # return func


def time_is(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print('{} cost: {}s'.format(func.__name__, end))
        return result
    return wrapper


def logged(level, logname=None, logmessage=None):
    def decorate(func):
        log_name = logname if logname else func.__module__
        log = logging.getLogger(log_name)
        log_message = logmessage if logmessage else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_message)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal log_message
            log_message = new_message
        return wrapper
    return decorate


@time_is
@logged(logging.DEBUG)
def countdown(n):
    while n >= 0:
        n -= 1


if __name__ == '__main__':
    # countdown(1000000)
    countdown.set_level(logging.WARN)
    countdown(1000000)

    countdown.set_message('call countdown')
    countdown(1000000)
