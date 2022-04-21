import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super(StructTupleMeta, cls).__init__(*args, **kwargs)
        for index, name in enumerate(cls._fields):
            setattr(cls, name, operator.itemgetter(index))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise TypeError('Expected {} arguments'.format(len(cls._fields)))
        return tuple.__new__(cls, args)


class Point(StructTuple):
    _fields = ['x', 'y']


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


if __name__ == '__main__':
    p = Point(10, 16)
    print(p)
    s = Stock('apple', 100, 99.8)
    print(s)