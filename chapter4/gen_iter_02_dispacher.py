# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_02_dispacher.py
# Time       ：2022/2/20 23:59
# Author     ：Zhong Lei
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    # __iter__()方法将迭代请求妆发给所有迭代对象。
    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for child in root:
        print(child)
