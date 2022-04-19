class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('can not be instantiate directly')


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok():
        print('Spam.grok')


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating spam')


if __name__ == '__main__':
    s = Spam()
    s2 = Spam()
    print(s is s2)
