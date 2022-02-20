# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_01_next.py
# Time       ：2022/2/20 22:19
# Author     ：Zhong Lei
"""

# 通过next() 函数访问可迭代对象中的元素，需要编写StopIteration异常
with open('C:\\Users\\86187\\cookbook\\chapter1\\data_struct_02.py', encoding='utf-8', errors='ignore') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        print('reading finished')


with open('C:\\Users\\86187\\cookbook\\chapter1\\data_struct_02.py', encoding='utf-8', errors='ignore') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
