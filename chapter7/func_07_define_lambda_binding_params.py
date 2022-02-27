# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_07_define_lambda_binding_params.py
# Time       ：2022/2/27 22:36
# Author     ：Zhong Lei
"""

funcs = [lambda x, n=n: x + n for n in range(5)]

for f in funcs:
    print(f(0))