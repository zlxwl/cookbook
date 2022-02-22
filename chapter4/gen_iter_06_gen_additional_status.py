# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_06_gen_additional_status.py
# Time       ：2022/2/22 21:41
# Author     ：Zhong Lei
"""
from collections import deque


# 如果生成器需要暴露属性并且与程序的其他部分交互，可以将迭代器定义在类里面。
class linehistory:
    def __init__(self, lines, histline=3):
        self.lines = lines
        self.history = deque(maxlen=histline)

    def __iter__(self):
        for lineno, line in enumerate(self.lines):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('gen_iter_01_next.py', 'r', encoding='utf-8', errors='ignore') as f:
    lines = linehistory(f)
    for line in lines:
        if 'iter' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
