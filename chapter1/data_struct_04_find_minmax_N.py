# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_04_find_minmax_N.py
# Time       ：2022/2/9 23:07
# Author     ：Zhong Lei
"""
import heapq

## 返回最大或者最小的N个数
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

## 使用key, 应对复杂数据结构。
portfolio = [
    {'name': 'IBM', 'share': 100, 'price': 91.1},
    {'name': 'APPL', 'share': 50, 'price': 543.22},
    {'name': 'FB', 'share': 200, 'price': 21.09},
    {'name': 'HPQ', 'share': 35, 'price': 31.75},
    {'name': 'YHOO', 'share': 45, 'price': 16.35},
    {'name': 'ACME', 'share': 75, 'price': 115.65}
]
print(heapq.nlargest(3, portfolio, key=lambda a: a['price']))
print(heapq.nsmallest(3, portfolio, key=lambda a: a['price']))


#
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
