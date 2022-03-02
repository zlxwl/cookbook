# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : yield_callback.py
# Time       ：2022/3/2 22:29
# Author     ：Zhong Lei
"""

def add(x, y):
    return x + y


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


from functools import wraps
from queue import Queue
def inline(func):
    @wraps(func)
    def wapper(*args):
        f = func(*args)
        queue = Queue()
        queue.put(None)
        while True:
            result = queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=queue.put)
            except StopIteration:
                break
    return wapper


@inline
def test():
    r = yield Async(add, (3, 4))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for i in range(10):
        r = yield Async(add, (i, i))
        print(r)

if __name__ == '__main__':
    test()