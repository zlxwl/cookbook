import inspect
import types
import time


class MultiMethod:
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, method):
        sig = inspect.signature(method)

        types = []
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            if param.annotation is inspect.Parameter.empty:
                raise TypeError('Argument {} must be annotated with a type'.format(name))
            if not isinstance(param.annotation, type):
                raise TypeError('Argument {} must be a type'.format(name))
            if param.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = method
            types.append(param.annotation)
        self._methods[tuple(types)] = method

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No matching method for types {}'.format(types))

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class MultiDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


class Spam(metaclass=MultipleMeta):
    def bar(self, x: int, y: int):
        print('bar_1:', x, y)

    def bar(self, s: str, n: int=0):
        print('bar_2:', s, n)


class Date(metaclass=MultipleMeta):
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)

    def __repr__(self):
        return str(self.day) + str(self.month) + str(self.year)

if __name__ == '__main__':
    # s = Spam()
    # s.bar(2, 3)
    # s.bar('hello')
    # s.bar('hello', 5)
    # s.bar(2, 'hello')
    # b = s.bar
    # print(b.__self__)
    # print(b.__func__)
    # print(b)
    d = Date(2012, 12, 21)
    print(d)
    e = Date()
    print(e.year)
    print(e.month)
    print(e.day)



