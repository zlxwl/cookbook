# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_25_weakvalue.py
# Time       ：2022/4/10 0:24
# Author     ：Zhong Lei
"""
import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

class Spam:
    manager = CachedSpamManager()

    def __init__(self):
        raise RuntimeError('Spam should not be initialized')

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

    @staticmethod
    def get_spam(name):
        return Spam.manager.get_spam(name)


if __name__ == '__main__':
    a = Spam.get_spam('foo')
    b = Spam.get_spam('bar')
    print(a is b)