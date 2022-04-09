# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_21_visit_3.py
# Time       ：2022/4/7 22:45
# Author     ：Zhong Lei
"""
import types
from chapter8.class_21_visit_1 import Node, Number, BinaryOperator, UnaryOperator, Add, Mul, Sub, Div, Negate

class Visit:
    def __init__(self, node):
        self.node = node

class NodeVisitor:
    def visit(self, node: Node):
        # stack = [node]
        stack = [Visit(node)]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result


    def _visit(self, node: Node):
        method_name = 'visit_' + type(node).__name__
        method =  getattr(self, method_name, None)
        if method is None:
            method = self.generic_visit
        return method(node)

    def generic_visit(self, node):
        raise RuntimeError('no {} method'.format('visit_' + type(node).__name__))


# class Evaluator(NodeVisitor):
#     def visit_Number(self, node: Number):
#         return node.value
#
#     def visit_Add(self, node: Add):
#         return self.visit(node.left) + self.visit(node.right)
#
#     def visit_Sub(self, node: Sub):
#         return self.visit(node.left) - self.visit(node.right)
#
#     def visit_Mul(self, node: Mul):
#         return self.visit(node.left) * self.visit(node.right)
#
#     def visit_Div(self, node: Div):
#         return self.visit(node.left) / self.visit(node.right)
#
#     def visit_Negate(self, node: Negate):
#         return -self.visit(node.operand)
class Evaluator(NodeVisitor):
    def visit_Number(self, node: Number):
        # yield node.value
        yield Visit(node.value)

    def visit_Add(self, node: Add):
        # yield (yield node.left) + (yield node.right)
        yield (yield Visit(node.left)) + (yield Visit(node.right))
    def visit_Sub(self, node: Sub):
        # yield (yield node.left) - (yield node.right)
        yield (yield Visit(node.left)) + (yield Visit(node.right))
    def visit_Mul(self, node: Mul):
        # yield (yield node.left) * (yield node.right)
        yield (yield Visit(node.left)) + (yield Visit(node.right))
    def visit_Div(self, node: Div):
        # yield (yield node.left) / (yield node.right)
        yield (yield Visit(node.left)) + (yield Visit(node.right))

    def visit_Negate(self, node: Negate):
        # yield -self.visit(node.operand)
        yield (yield Visit(-node.operand))



if __name__ == '__main__':
    # t1 = Sub(Number(3), Number(4))
    # t2 = Mul(Number(2), t1)
    # t3 = Div(t2, Number(5))
    # t4 = Add(Number(1), t3)
    # e  = Evaluator()
    # print(e.visit(t4))

    a = Number(0)
    for x in range(1, 10000):
        a = Add(a, Number(x))
    e = Evaluator()
    print(e.visit(a))