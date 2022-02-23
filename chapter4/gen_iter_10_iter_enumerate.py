# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_10_iter_enumerate.py
# Time       ：2022/2/23 20:54
# Author     ：Zhong Lei
"""
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 1 表示索引位置
for idx, val in enumerate(my_list, 1):
    print(idx, val)


def parse_data(filename):
    with open(filename, encoding='utf-8', errors='ignore') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

# 统计单词
from collections import defaultdict

word_summary = defaultdict(list)

with open('word.txt', 'r') as f:
    lines = f.readlines()
    for lineno, line in enumerate(lines):
        for word in line.split():
            word_summary[word].append[lineno]