from inspect import Signature, Parameter
import inspect


def make_sig(*names):
    return Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names])


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            # print('{}: {}'.format(name, value))
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


if __name__ == '__main__':
    print(inspect.signature(Stock))
    s1 = Stock('ACME', 100, 490.1)
    s1 = Stock('ACME', 490.1)


