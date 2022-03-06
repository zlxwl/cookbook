# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_05_private.py
# Time       ：2022/3/3 22:31
# Author     ：Zhong Lei
"""

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass



class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print('bb')

    def public_method(self):
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        print('cc')


if __name__ == '__main__':
    c = C()
    c._C__private_method()
    c._B__private_method()
    b = B()
    b.public_method()