import types
import abc


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price

cls_dict = {'__init__': __init__, 'cost': cost}
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__


# class Spam(Base, debug=True, typecheck=False):
#     pass
#
#
# types.new_class('Spam', (Base,),
#                 {'debug': False, 'typecheck': False},
#                 lambda ns: ns.update(cls_dict))


if __name__ == '__main__':
    s = Stock('apple', 100, 99.9)
    print(s.cost())
    print(Stock)
    print(type(Stock))