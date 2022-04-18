import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print('time cost {}'.format(end))
        return result
    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n >= 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n >= 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n >= 0:
            n -= 1


from abc import abstractmethod, ABCMeta
class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass


if __name__ == '__main__':
    Spam().instance_method(100000)
    Spam.static_method(100000)
    Spam.class_method(100000)
