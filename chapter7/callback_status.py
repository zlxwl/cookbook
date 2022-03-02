# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : callback_status.py
# Time       ：2022/3/2 21:27
# Author     ：Zhong Lei
"""
def add(x, y):
    return x + y


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


# class方案
class Result:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

result = Result()
apply_async(add, (3, 4), callback=result.handler)
apply_async(add, ('hello', 'world'), callback=result.handler)


# 闭包方案
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got-{}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (3, 4), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)


# 协程方案
def make_handler():
    sequence = 0
    while True:
        sequence += 1
        result = yield
        print('[{}] Got--{}'.format(sequence, result))

handler = make_handler()
next(handler)
apply_async(add, (3, 4), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)


# 额外参数
from functools import partial
class sequenceno:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got++ {}'.format(seq.sequence, result))

seq = sequenceno()
apply_async(add, (3, 4), callback=partial(handler, seq=seq))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))
apply_async(add, (3, 4), callback=lambda result, seq=seq: handler(result, seq))
apply_async(add, ('hello', 'world'), callback=lambda result, seq=seq: handler(result, seq))

