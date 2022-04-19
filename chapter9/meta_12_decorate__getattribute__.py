

def log_getattribute(cls):
    original_attr = cls.__getattribute__

    def new_attr(self, x):
        print('getting {}'.format(x))
        return original_attr(self, x)

    cls.__getattribute__ = new_attr
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


if __name__ == '__main__':
    a = A(5)
    a.x
    a.spam()
