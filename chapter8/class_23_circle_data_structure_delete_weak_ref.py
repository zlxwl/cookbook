# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_23_circle_data_structure_delete_weak_ref.py
# Time       ：2022/4/9 17:55
# Author     ：Zhong Lei
"""
class Data:
    def __del__(self):
        print('Data.__del__')


class Node:
    def __init__(self):
        self.value = Data()
        self.parent = None
        self.children = []

    def add_children(self, child):
        self.children.append(child)
        child.parent = self

    def __del__(self):
        del self.value
        del self.parent
        del self.children


if __name__ == '__main__':
    # a = Data()
    # del a
    #
    # a = Node()
    # del a

    a = Node()
    import weakref
    a_ref = weakref.ref(a)
    print(a_ref)
    print(a_ref())
    del a
    print(a_ref())