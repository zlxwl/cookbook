# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_24_sourcecode.py
# Time       ：2022/4/23 21:43
# Author     ：Zhong Lei
"""
import ast
import inspect


class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name) for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')
        node.body[:0] = code_ast.body
        self.func = node


def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break
        src = '\n'.join(srclines[n+1:])
        if src.startswith((' ', '\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        c1 = NameLower(namelist)
        c1.visit(top)

        temp = {}
        exec(compile(top, '', 'exec'), temp, temp)

        func.__code__ = temp[func.__name__].__code__
        return func
    return lower


INCR = 1

@lower_names('INCR')
def countdown(n):
    while n>0:
        n -= INCR


if __name__ == '__main__':
    countdown(100000)