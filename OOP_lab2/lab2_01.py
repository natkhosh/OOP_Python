# TODO:
#  + 1. Атрибут класса
#  + 1.1 Публичный атрибут класса
#  + 1.2 Приватный атрибут класса "_"
#  + 1.1 Защищеный атрибут класса "__"
#  + 2. Атрибут экземпляра
#  + 2.1 Публичный атрибут экземпляра
#  + 2.2 Приватный атрибут экземпляра
#  + 2.1 Защищеный атрибут экземпляра
#  + 3. Метод экземпляра
#  + 3.1 Публичный метод экземпляра
#  + 3.2 Приватный метод экземпляра
#  + 3.3 Защищеный метод экземпляра
#  4. Метод класса
#  4.1 Публичный метод класса
#  4.2 Приватный метод класса
#  4.3 Защищеный метод класса
#  5. Статический метод
#  5.1 Публичный статический метод
#  5.2 Приватный статический метод
#  5.3 Защищеный статический метод
#  6. Сделать наследника и через него проверить область видимости предка (т.е всё то, что было реализовано в классе A)


class A:
    public_class_attr_A = 'public_class_attr_A'
    _protected_class_attr_A = 'protected_class_attr_A'
    __privat_class_attr_A = 'privat_class_attr_A'

    def __init__(self):
        self.public_object_attr_A = 'public_object_attr_A'
        self._protected_object_attr_A = 'protected_object_attr_A'
        self.__privat_object_attr_A = 'privat_object_attr_A'

    @property
    def public_object_method_(self):
        print('public_object_method')
        return self.public_object_attr_A

    @property
    def protected_object_method(self):
        print('protected_object_method')
        return self._protected_object_attr_A

    @property
    def privat_object_method(self):
        print('privat_object_method')
        return self.__privat_object_attr_A

    @staticmethod
    def public_object_method__static():
        print('staticmethod_public_object_method')

    @staticmethod
    def protected_object_method_static():
        print('staticmethod_protected_object_method')

    @staticmethod
    def privat_object_method_static():
        print('staticmethod_privat_object_method')

    @classmethod
    def public_object_method_classmeth(cls):
        print(cls.public_class_attr_A)
        return cls

    @classmethod
    def protected_object_method_classmeth(cls):
        print(cls._protected_class_attr_A)
        return cls

    @classmethod
    def privat_object_method_classmeth(cls):
        print(cls.__privat_class_attr_A)
        return cls

    def public_object_method_O(self):
        print('public_object_method')

    def protected_object_method_O(self):
        print('protected_object_method')

    def privat_object_method_O(self):
        print('privat_object_method')

    def __str__(self):
        return f'{self.public_object_attr_A}'


class B(A):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    #  Класс А (предок)
    a = A()
    # Атрибуты класса:
    # 1. Публичный атрибут класса - можно получить
    print(a.public_class_attr_A, '\n')

    # 2. Защищенный атрибут класса - можно получить
    print(a._protected_class_attr_A, '\n')

    # 3. Приватный атрибут класса - только для внутреннего использования
    # print(a.__private_class_attr_A)
    print(a._A__privat_class_attr_A, '\n')

    # Атрибуты экземпляра класса:
    # 1. Публичный атрибут экземпляра класса - можно получить
    print(a.public_object_attr_A)

    # 2. Защищенный атрибут экземпляра класса - можно получить
    print(a._protected_object_attr_A)

    # 3. Приватный атрибут экземпляра класса - доступ только через Property и setter
    # print(a.__private_object_attr_A)
    print(a.privat_object_method)
    print('-----------')
    a.public_object_method_classmeth()
    # print(a.public_object_method_)


    print('-****-')

    #  Класс В (потомок), наследующий класс А

    b = B()

    # Атрибуты класса:
    # 1. Публичный атрибут класса - можно получить
    print(b.public_class_attr_A, '\n')

    # 2. Защищенный атрибут класса - можно получить
    print(b._protected_class_attr_A, '\n')

    # 3. Приватный атрибут класса - только для внутреннего использования
    # print(a.__private_class_attr_A)
    print(b._A__privat_class_attr_A, '\n')

    # Атрибуты экземпляра класса:
    # 1. Публичный атрибут экземпляра класса - можно получить
    print(b.public_object_attr_A)

    # 2. Защищенный атрибут экземпляра класса - можно получить
    print(b._protected_object_attr_A)

    # 3. Приватный атрибут экземпляра класса - доступ только через Property и setter
    # print(b.__private_object_attr_A)

    print('-----------')
    # property
    print(b.public_object_method_, '\n')
    print(b.protected_object_method, '\n')
    print(b.privat_object_method, '\n')

    print('-----------')
    # staticmethod
    b.public_object_method__static()
    b.protected_object_method_static()
    b.privat_object_method_static()

    print('-----------')
    # classmethod
    b.public_object_method_classmeth()          # возвращает атрибут класса предка
    b.protected_object_method_classmeth()       # возвращает атрибут класса предка
    b.privat_object_method_classmeth()          # возвращает атрибут класса предка

    print('-----------')
    # object methods
    b.public_object_method_O()
    b.protected_object_method_O()
    b.privat_object_method_O()