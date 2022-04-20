class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('bad attribute name:' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    pass


class B(Root):
    def bar(self):
        pass

    # def barB(self):
    #     pass

if __name__ == '__main__':
    b = B()