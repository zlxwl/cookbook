class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('can not be instantiate directly')


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok():
        print('Spam.grok')


if __name__ == '__main__':
    Spam.grok()
    Spam()