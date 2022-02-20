# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_19_trainsfer.py
# Time       ：2022/2/20 21:25
# Author     ：Zhong Lei
"""
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)


import os
files = os.listdir('C:\\Users\\86187\\cookbook\\chapter1')
if any(name.endswith('.py') for name in files):
    print('python')
else:
    print('no python')


s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))


portfolio = [
    {'name': 'GOOD', 'share': 50},
    {'name': 'YAHOO', 'share': 75},
    {'name': 'AOL', 'share': 20},
    {'name': 'SCOX', 'share': 65}
]
min_shares = min(s['name'] for s in portfolio)
print(min_shares)
min_shares = min(portfolio, key=lambda p: p['name'])
print(min_shares)






