class LoggedGetAttribute:
    def __getattribute__(self, name):
        print('getting', name)
        return super().__getattribute__(name)

    def __getattr__(self, item):
        # if hasattr(self, item):
        #     print(item)
        # else:
        print('missed {}'.format(item))


class A(LoggedGetAttribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


if __name__ == '__main__':
    a = A(40)
    a.x
    a.spam()
    a.y
