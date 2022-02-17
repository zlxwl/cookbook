# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_18_named_tuple.py
# Time       ：2022/2/17 22:28
# Author     ：Zhong Lei
"""
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'share', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.share * s.price
    return total

# namedtuple是不可变的需要使用_replace()方法来替代。
s = Stock(name='ACME', share='SHARE', price=123.45)
print(s)
s._replace(price=12)
b = s._replace(price='44')
print(b)

# 利用_replace(**s) s是dict类型来进行字典拆包； nametuple不适合用来存贮经常需要修改的数据。
Stock = namedtuple('Stock', ['name', 'share', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'share': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'share': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))


