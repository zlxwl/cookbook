class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('value must be str')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('attr {} can not be delete'.format(self._name))

p = Person('Json')
print(p.name)
p.name = 'kate'
print(p.name)


class SubPerson(Person):
    @property
    def name(self):
        print('gettin name')
        super().name

    @name.setter
    def name(self, value):
        print('setting name to {}'.format(value))
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting')
        super(SubPerson, SubPerson).name.__delete__(self)

sub = SubPerson('java')
print(sub.name)

# descriptor方案
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected str')
        instance.__dict__[self.name] = value


class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to {}'.format(value))
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


sub = SubPerson('a')
print(sub.name)

sub.name = 'b'
print(sub.name)
