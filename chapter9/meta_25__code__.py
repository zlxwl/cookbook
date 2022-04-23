# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_25__code__.py
# Time       ：2022/4/23 22:57
# Author     ：Zhong Lei
"""
import types


def add(x, y):
    return x + y


if __name__ == '__main__':
    c = add.__code__
    print(c)
    print(c.co_code)
    newbytes = b'xxxxxxx'
    nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount, c.co_nlocals, c.co_stacksize, c.co_flags,
                        newbytes,
                        c.co_consts, c.co_names, c.co_varnames, c.co_filename, c.co_name, c.co_firstlineno, c.co_lnotab)
    print(nc)

    add.__code__ = nc
    add(2, 3)
