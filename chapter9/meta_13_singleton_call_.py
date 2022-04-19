# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_13_singleton_call_.py
# Time       ：2022/4/19 21:37
# Author     ：Zhong Lei
"""
import weakref
class Cache(type):
    def __init__(self, *args, **kwargs):
        super(Cache, self).__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam(metaclass=Cache):
    def __init__(self, name):
        print('initial spam ({!r})'.format(name))
        self.name = name


if __name__ == '__main__':
    s1 = Spam()
    s2 = Spam()
    print(s1 is s2)
    print(s1 or s2)