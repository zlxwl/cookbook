from abc import ABCMeta, abstractmethod


class IOStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, max_bytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IOStream):
    def read(self, max_bytes=-1):
        pass

    def write(self, data):
        pass


# 类型检查
def serialize(obj, SocketStream):
    if not isinstance(obj, SocketStream):
        raise TypeError('Expected')
    return True

s = SocketStream()
print(serialize(s, IOStream))


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self):
        pass

    @name.deleter
    @abstractmethod
    def name(self):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


import collections
obj = ''
if isinstance(obj, collections.Sequence):
    print()
if isinstance(obj, collections.Mapping):
    print()
if isinstance(obj, collections.Iterable):
    print()

