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