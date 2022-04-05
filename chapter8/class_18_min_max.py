# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_18_min_max.py
# Time       ：2022/4/4 16:34
# Author     ：Zhong Lei
"""
from collections import UserDict

class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, key):
        print('getting {}'.format(key))
        super(LoggedMappingMixin, self).__getitem__(key)

    def __setitem__(self, key, value):
        print('setting {} = {!r}'.format(key, value))
        super(LoggedMappingMixin, self).__setitem__(key, value)

    def __delete__(self, instance):
        print('deleting {}'.format(instance))
        super(LoggedMappingMixin, self).__delete__(instance)


class SetOnceMappingMixin:
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        super(SetOnceMappingMixin, self).__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super(StringKeysMappingMixin, self).__setitem__(key, value)


class LoggerDict(LoggedMappingMixin, UserDict):
    pass


from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


from collections import OrderedDict
class StringOrderDict(StringKeysMappingMixin, SetOnceMappingMixin, OrderedDict):
    pass


class RestrictKeyMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self._restrict_key_type = _restrict_key_type
        super(RestrictKeyMixin, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self._restrict_key_type):
            raise KeyError('key must be {}'.format(self._restrict_key_type))
        super(RestrictKeyMixin, self).__setitem__(key, value)


class RDict(RestrictKeyMixin, dict):
    pass

if __name__ == '__main__':
    logdict = LoggerDict()
    logdict['x'] = 23

    print(logdict['x'])
    # del logdict['x']

    # s = SetOnceDefaultDict(list)
    # s['x'].append(2)
    # s['y'].append(3)
    # s['z'].append(10)
    # s['x'] = 40

    # o = StringOrderDict()
    # o['x'] = 23
    # o[42] = 10
    # print(o)
    # o['x'] = 50

    #
    # r = RDict(_restrict_key_type=str)
    # e = RDict([('name', 'Dave'), ('n', 37)],_restrict_key_type=str)
    # f = RDict(name='Dave', n=37, _restrict_key_type=str)
    # print(f)
    # print(e)
