# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_01_args.py
# Time       ：2022/2/24 20:40
# Author     ：Zhong Lei
"""
import html

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    print(keyvals)
    attr_str = ''.join(keyvals)

    element = '<{name}{attrs}>{value}</name>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))
