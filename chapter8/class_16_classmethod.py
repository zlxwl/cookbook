# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_16_classmethod.py
# Time       ：2022/3/23 21:58
# Author     ：Zhong Lei
"""
import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return 'year:{}-month:{}-day:{}'.format(self.year, self.month, self.day)

d1 = Date(2022, 3, 22)
print(d1)
d2 = Date.today()
print(d2)
