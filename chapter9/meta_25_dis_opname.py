# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_25_dis_opname.py
# Time       ：2022/4/23 22:42
# Author     ：Zhong Lei
"""
import dis
import opcode


def generate_opcodes(codebytes):
    extended_args = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op > opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i+1] * 256 + extended_args
            extended_args = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_args = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)


def countdown(n):
    while n > 0:
        print('t-minus')
        n -= 1


if __name__ == '__main__':
    for op, oparg in generate_opcodes(countdown.__code__.co_code):
        print(op, opcode.opname[op], oparg)