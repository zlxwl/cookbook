class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('can not be instantiate directly')


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok():
        print('Spam.grok')


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super(Singleton, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating spam')


if __name__ == '__main__':
    s = Spam()
    s2 = Spam()
    print(s is s2)
