# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_15_groupby.py
# Time       ：2022/2/14 22:24
# Author     ：Zhong Lei
"""
from itertools import groupby
from operator import itemgetter

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 必须先排序
rows.sort(key=itemgetter('date'))
for data, items in groupby(rows, key=itemgetter('date')):
    print(data)
    for i in items:
        print(i)

# 不排序可以使用defaultdict
from collections import defaultdict

row_by_data = defaultdict(list)
for row in rows:
    row_by_data[row['date']].append(row)
print(row_by_data)