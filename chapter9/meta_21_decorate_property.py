class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be str')
        self._name = value

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be int')
        self._age = value

    def __repr__(self):
        return self.name + str(self.age)


if __name__ == '__main__':
    p = Person('mike', 18)
    print(p)
    p.name = 'jason'
    print(p)
    p.name = 19

