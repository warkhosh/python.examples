# more info: https://tirinox.ru/useful-decorators/


class Person(object):
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._age = None
        self._sex = None

    @property
    def full_name(self):
        return "%s %s" % (self._first_name, self._last_name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = int(value)

    @age.deleter
    def age(self):
        self._age = None

    @staticmethod
    def help():
        print("Current class:", __class__.__name__)

    """ 
    Другое варанит: при явных методах
    """

    def get_sex(self):
        return self._sex

    def set_sex(self, value):
        self._sex = str(value)

    def del_sex(self):
        self._sex = None

    sex = property(get_sex, set_sex, del_sex, 'Это свойство sex!')


user = Person('Konstantin', 'Egorov')
user.age = 39
user.sex = "male"

print("User:", user.full_name)
print("Age:", user.age)
print("Sex:", user.sex)

user.help()

del user.age
del user.sex

print("\nNEW VALUES:")
print("User:", user.full_name)
print("Sex:", user.sex)
print("Age:", user.age)