# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_17__new__.py
# Time       ：2022/3/23 22:22
# Author     ：Zhong Lei
"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return 'year{}-month{}-day{}'.format(self.year, self.month, self.day)

d = Date.__new__(Date)
data = {'year': 2022, 'month': 3, 'day': 22}

for key, value in data.items():
    setattr(d, key, value)

print(d)


from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = Date.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

    def __str__(self):
        return 'year{}-month{}-day{}'.format(self.year, self.month, self.day)


d = Date.today()
print(d)