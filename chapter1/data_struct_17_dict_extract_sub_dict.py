# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_17_dict_extract_sub_dict.py
# Time       ：2022/2/16 22:25
# Author     ：Zhong Lei
"""

prices = {
    'ACME': 45.23,
    'APPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}
tec_name = ['APPL', 'IBM', 'HPQ', 'MSFT']
P2 = {key: value for key, value in prices.items() if value in tec_name}

# tuple
p1 = dict((key, value) for key, value in prices.items() if value>200)
print(p1)