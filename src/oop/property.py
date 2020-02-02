# more info: https://tirinox.ru/useful-decorators/


class Person(object):
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return "%s %s" % (self._first_name, self._last_name)


user = Person('Konstantin', 'Egorov')
print("User:", user.full_name)