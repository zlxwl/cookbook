# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_10_callback_status.py
# Time       ：2022/2/28 22:41
# Author     ：Zhong Lei
"""

# example 1
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got', result)


def add(x, y):
    return x + y

apply_async(add, (3, 4), callback=print_result)

# example  class
# class ResultHandler:
#     def __init__(self):
#         self.sequence = 0
#
#     def handler(self, result):
#         self.sequence += 1
#         print('[{}] Got: {}'.format(self.sequence, result))
#
#
# r = ResultHandler()
# apply_async(add, (3, 4), callback=r.handler)
# apply_async(add, (3, 4), callback=r.handler)


# nonlocal 关键字引用闭包中定义的局部变量
# def make_handler():
#     sequence = 0
#     def handler(result):
#         nonlocal sequence
#         sequence += 1
#         print('[{}] Got: {}'.format(sequence, result))
#     return handler
# apply_async(add, (3, 4), callback=make_handler)
# apply_async(add, (3, 4), callback=make_handler)


# 协程中的send方法
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, (2, 3), callback=handler.send)


#
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got- {}'.format(seq.sequence, result))

from functools import partial

seq = SequenceNo()
# apply_async(add, (2, 3), callback=partial(handler, seq=seq))
# apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, (2, 3), callback=lambda result, seq=seq: handler(result, seq))
apply_async(add, (2, 3), callback=lambda result, seq=seq: handler(result, seq))
