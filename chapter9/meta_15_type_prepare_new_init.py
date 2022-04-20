from abc import abstractmethod, ABCMeta


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, name):
        pass

    @abstractmethod
    def write(self, data):
        pass


class Mymeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, *,
                    debug=False, synchronize=True):
        print('enter __prepare__')
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=True):
        print('enter __new__')
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, synchronize=True):
        print('enter __init__')
        return super().__init__(name, bases, ns)


class Spam(metaclass=Mymeta, debug=False, synchronize=True):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.name)


if __name__ == '__main__':
    s = Spam('mike')
    print(s)
    print(Spam.print_meta_info())

