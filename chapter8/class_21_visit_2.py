# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_21_visit_2.py
# Time       ：2022/4/7 21:29
# Author     ：Zhong Lei
"""
from chapter8.class_21_visit import Sub, Add, Mul, Div, Number, Negate, Node


class NodeVisitor:
    def visit(self, node: Node):
        method_name = 'visit_' + type(node).__name__
        if getattr(self, method_name):
            method = getattr(self, method_name)
        else:
            method = self.generic_visit
        return method(node)

    def generic_visit(self, node: Node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_Number(self, node: Number):
        return node.value

    def visit_Add(self, node: Add):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node: Sub):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node: Mul):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node: Div):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node: Negate):
        return -node.opreand


if __name__ == '__main__':
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    e  = Evaluator()
    print(e.visit(t4))