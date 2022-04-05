# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_21_visit_1.py
# Time       ：2022/4/5 22:19
# Author     ：Zhong Lei
"""
# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_21_visit.py
# Time       ：2022/4/5 21:55
# Author     ：Zhong Lei
"""
class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node: Node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name)
        if method is None:
            method = self.generic_visit
        return method(node)

    def generic_visit(self, node: Node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_Number(self, node: Node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return  -node.operand


if __name__ == '__main__':
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    e  = Evaluator()
    print(e.visit(t4))



