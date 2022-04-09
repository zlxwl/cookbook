# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_25_WeakValueDictionary.py
# Time       ：2022/4/9 23:31
# Author     ：Zhong Lei
"""
import weakref


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self

    def __init__(self, name):
        print('initialize Spam')
        self.name = name


if __name__ == '__main__':
    s = Spam('Dave')
    t = Spam('Dave')
    print(s is t)