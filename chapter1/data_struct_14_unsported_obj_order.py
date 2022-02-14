# sorted 中的key关键字可以传入callable对象；
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    Users = [User(23), User(3), User(99)]
    print(Users)
    print(sorted(Users, key=lambda u:u.user_id))

sort_notcompare()

from operator import attrgetter
Users = [User(23), User(3), User(99)]
print(sorted(Users, key=attrgetter('user_id')))

# attrgetter() 支持多个关键字。 sorted, min, max都支持这种操作。