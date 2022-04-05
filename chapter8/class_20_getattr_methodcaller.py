# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_20_getattr_methodcaller.py
# Time       ：2022/4/5 20:57
# Author     ：Zhong Lei
"""
import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

    def __repr__(self):
        return 'Point({!r}, {!r})'.format(self.x, self.y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)
print(d)

# 查找在字符串中的方法
d = operator.methodcaller('distance', 0, 0)(p)
print(d)


points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2),
]
points.sort(key=operator.methodcaller('distance', 0, 0))
# points.sort(key=getattr(p, 'distance')(0, 0))
# print(points)
