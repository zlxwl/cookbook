# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_12_closure_stimulate_class.py
# Time       ：2022/3/1 23:18
# Author     ：Zhong Lei
"""
import sys
class ClosureInstence:
    def __init__(self, locals=None):
        if locals == None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstence()


s = Stack()
s.push(10)
s.push(20)
s.push('hello')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())