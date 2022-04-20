from inspect import signature
import logging


class MatchSignatureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            pre_dfn = getattr(sup, name, None)
            if pre_dfn:
                prev_sig = signature(pre_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('signature mismatch in '
                                    '%s. %s != %s',
                                    value.__qualname__,
                                    prev_sig,
                                    val_sig)


class Root(metaclass=MatchSignatureMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass


if __name__ == '__main__':
    b = B()
