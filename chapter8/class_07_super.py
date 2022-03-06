class A:
    def spam(self):
        print('spam A')


class B(A):
    def spam(self):
        print('spam B')
        super().spam()

a = A()
a.spam()
b = B()
b.spam()


class A:
    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

a = A()
print(a.x)
b = B()
print(b.x, b.y)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __setattr__(self, key, value):
        if key.startswith('-'):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)

    def __getattr__(self, name):
        return getattr(self._obj, name)


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        Base.__init__(self)
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')

c = C()
print(C.__mro__)


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')


c = C()
print(C.__mro__)


class A:
    def __init__(self):
        print('A.spam')


class B:
    def spam(self):
        print('B.spam')


class C(A, B):
    pass

c = C()
c.spam()