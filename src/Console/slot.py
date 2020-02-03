# __slots__
# Позволяет задать ограниченный набор атрибутов, которыми будет обладать экземпляр класса.
# Иными словами это уменьшает расход ресурсов для скрипта за счет не создание директивы __dict__


class UserClass(object):
    __slots__ = ('first_name', 'last_name')


if __name__ == "__main__":
    user = UserClass()
    user.first_name = "Vladimir"
    user.last_name = "Lenin"

    print("first_name = ", user.first_name)
    print("last_name = ", user.last_name)

    try:
        # Проверяем что
        user.patronymic_name = "Ilyich"
        print("attr = ", user.__dict__)

    except BaseException as e:
        print("We get an error that such an attribute cannot be created:", e)

    finally:
        pass
