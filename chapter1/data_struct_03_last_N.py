# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_03_last_N.py
# Time       ：2022/2/9 22:40
# Author     ：Zhong Lei
"""
from collections import deque

# d.pop(), d.popleft(), d.append(), d.appendleft()
def search(lines, pattern, history=5):
    previous = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous
        previous.append(line)


if __name__ == '__main__':
    with open('somefile.txt', 'r') as f:
        for line, previous in search(f, 'python', 5):
            for pline in previous:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
