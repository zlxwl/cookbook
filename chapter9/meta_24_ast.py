# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : meta_24_ast.py
# Time       ：2022/4/23 20:09
# Author     ：Zhong Lei
"""
import ast


# ex = ast.parse('2 + 3*4 + x', mode='eval')
# print(ex)
# ast.dump(ex)
class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Delete):
            self.deleted.add(node.id)


if __name__ == '__main__':
    code = '''for i in range(10): print(i)'''
    top = ast.parse(code, mode='exec')
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)
    exec(compile(top, '<stdin>', 'exec'))

