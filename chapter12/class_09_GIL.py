# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_09_GIL.py
# Time       ：2022/3/26 22:40
# Author     ：Zhong Lei
"""
pool = None


def some_word(*args):
    return sum(args)

def thread():
    while True:
        r = pool.apply(some_word, [55, 10, 99])
        print(r)

if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    thread()