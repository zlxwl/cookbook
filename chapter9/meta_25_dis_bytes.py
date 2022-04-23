# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_25_dis_bytes.py
# Time       ：2022/4/23 22:30
# Author     ：Zhong Lei
"""
import dis
import opcode


def countdown(n):
    while n > 0:
        print('T-minus')
        n -= 1


if __name__ == '__main__':
    dis.dis(countdown)
    c = countdown.__code__.co_code
    print(opcode.opname[c[0]])
    print(opcode.opname[c[1]])