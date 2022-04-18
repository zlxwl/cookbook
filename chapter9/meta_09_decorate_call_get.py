import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print('bar', x)


def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper


@profiled
def countdown(n):
    while n >= 0:
        n -= 1

if __name__ == '__main__':
    print(add(2, 3))
    print(add(4, 5))
    print(add.ncalls)

    b = Spam()
    b.bar(1)
    b.bar(2)
    b.bar(3)
    print(Spam.bar.ncalls)

    countdown(100)
    countdown(200)
    print(countdown.ncalls())