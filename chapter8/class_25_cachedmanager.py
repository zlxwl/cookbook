import weakref


class CachedManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedManager()

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_spam(name):
        return Spam.manager.get_spam(name)


if __name__ == '__main__':
    # 无法防止类进行实例化.
    a = Spam.get_spam('foo')
    b = Spam.get_spam('foo')
    print(a is b)