from functools import wraps


class A:
    def decorate_1(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print('decorate_1')
            return func(*args, **kwargs)
        return wraps

    @classmethod
    def decorate_2(cls, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print('decorate_2')
            return func(*args, **kwargs)
        return wrap

a = A()


@a.decorate_1
def add(x, y):
    return x + y


@A.decorate_2
def spam():
    print('spam')


class B(A):
    @A.decorate_2
    def bar(self):
        print('bar')

if __name__ == '__main__':
    b = add(2, 3)
    c = spam()

    b = B()
    b.bar()


