# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_struct_07_keep_dict_ordered.py
# Time       ：2022/2/11 23:12
# Author     ：Zhong Lei
"""
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
import json
print(json.dumps(d))
