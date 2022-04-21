import operator
import types
import sys


def named_tuple(classname, fieldnames):
    cls_dict = {name: property(operator.itemgetter(index)) for index, name in enumerate(fieldnames)}

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(classname, (tuple), {}, lambda ns:ns.update(cls_dict))

    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


if __name__ == '__main__':
    Stock = named_tuple('Stock', ['name', 'shares', 'price'])
    s = Stock('apple', 100, 99)
    print(s)