# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_23_circle_data_structure.py
# Time       ：2022/4/9 17:15
# Author     ：Zhong Lei
"""
import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_children(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    root = Node('root')
    c1 = Node('child')
    root.add_children(c1)

    print(c1.parent)
    del root
    print(c1.parent)