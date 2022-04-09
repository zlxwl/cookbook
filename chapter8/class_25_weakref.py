# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_25_weakref.py
# Time       ：2022/4/9 22:40
# Author     ：Zhong Lei
"""
import weakref


class Spam:
    def __init__(self, name):
        self.name = name

_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


if __name__ == '__main__':
    a = get_spam('foo')
    b = get_spam('bar')
    c = get_spam('foo')

    print(a is c)
