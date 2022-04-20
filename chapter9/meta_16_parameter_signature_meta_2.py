from inspect import Signature, Parameter
import inspect


def make_sig(*names):
    sig = Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names])
    return sig


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_value = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_value.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'price', 'shares']

    # def __init__(sel
    # f, name, price, shares):
    #     self.name = name
    #     self.price = price
    #     self.shares = shares

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)


class Piont(Structure):
    _fields = ['x', 'y']


if __name__ == '__main__':
    s = Stock('apple', 40)
    print(inspect.signature(s))
    print(inspect.signature(s).parameters)


