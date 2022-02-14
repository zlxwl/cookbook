# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_08_dict_calculate.py
# Time       ：2022/2/12 22:08
# Author     ：Zhong Lei
"""
prices = {
    'ACME': 45.23,
    'APPLE': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 先比较value , 后比较key，但是zip是生成器只能被调用一次。
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
sorted_price = sorted(zip(prices.values(), prices.keys()))
print(sorted_price)


# 这种方法要多执行一步
min_key = min(prices, key=lambda k: prices[k])
print(min_key)
min_price = prices[min_key]
print(min_price)
