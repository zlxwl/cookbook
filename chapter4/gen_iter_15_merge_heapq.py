# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_15_merge_heapq.py
# Time       ：2022/2/23 21:58
# Author     ：Zhong Lei
"""
# 必须保证迭代的每个序列都是有序的
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)

with open('pwd', 'r', encoding='utf-8', errors='ignore') as file1, \
        open('gen_iter_01_next.py', 'r', encoding='utf-8', errors='ignore') as file2, \
        open('out.txt', 'w', encoding='utf-8', errors='ignore') as f:
    for line in heapq.merge(file1, file2):
        f.write(line)


