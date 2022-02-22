# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_05_reversed.py
# Time       ：2022/2/22 21:27
# Author     ：Zhong Lei
"""

# 1.对象必须拥有可确定的大小， 2.实现了__reversed__()
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)


# 实现了__reversed__() 方法可以在自定义的类上实现反向迭代
class Countdown:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        n = self.value
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.value:
            yield n
            n += 1

# 无需将数据转换为列表直接进行反向迭代，节约内存。
c = Countdown(5)
for number in c:
    print(number)

for number in reversed(c):
    print(number)




