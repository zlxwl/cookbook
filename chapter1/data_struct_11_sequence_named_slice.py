# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_11_sequence_named_slice.py
# Time       ：2022/2/13 23:05
# Author     ：Zhong Lei
"""
# 用切片代替硬编码
record = '..................100..........513.25.....'
# SHARES = record[18:21]
# PRICE = record[31:37]
SHARES = slice(18, 21)
PRICE = slice(31, 37)
cost= int(record[SHARES]) * float(record[PRICE])
print(cost)


s = 'HelloWorld'
a = slice(5, 10, 2)
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])

