# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_02.py
# Time       ：2022/2/9 21:29
# Author     ：Zhong Lei
"""
import math


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *arg in records:
    if tag == 'foo':
        do_foo(*arg)
    elif tag == 'bar':
        do_bar(*arg)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

items = [1, 2, 3, 4, 5]
head, *tail = items
print(tail)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

if __name__ == '__main__':
    print(drop_first_last([100, 200, 300, 500]))