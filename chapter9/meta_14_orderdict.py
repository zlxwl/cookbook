from collections import OrderedDict


class Typed:
    _expect_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expect_type):
            raise TypeError('expected' + str(self._expect_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expect_type = int


class Float(Typed):
    _expect_type = float


class String(Typed):
    _expect_type = str


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in d.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, clsname, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError('{} already definded in {}'.format(key, self.clsname))
        super().__setitem__(key, value)


class OrderMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return NoDupOrderedDict(clsname)


class A(metaclass=OrderMeta):
    def spam(self):
        pass

    def spam(self):
        pass


if __name__ == '__main__':
    s = Stock('good', 100, 490.1)
    print(s.name)
    print(s.as_csv())

    a = A()