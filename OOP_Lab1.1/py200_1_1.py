# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Мокрушина Н.Ю.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class Glass:
    """"Класс Glass это модель стакана.
    Аттрибуты:
    capacity_volume - максимальный объем стакана
    occupied_volume - Текущий объем стакана
     Методы:
    get_self_id - возвращает идентификатор экземпляра класса в шестнадцатеричном виде
    """
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

    def get_self_id(self):
        """"
        :return - возвращает идентификатор экземпляра класса в шестнадцатеричном виде
        """
        return hex(id(self))        # для 8-й задачи


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

print('\n2. >')
glass_2_1 = Glass(200, 100)     # экземпляр класса
print(f'glass_2_1: capacity_volume - {glass_2_1. capacity_volume}')
print(f'glass_2_1: occupied_volume - {glass_2_1. occupied_volume}')

glass_2_2 = Glass(500, 50)     # экземпляр класса
print(f'glass_2_2: capacity_volume - {glass_2_2. capacity_volume}')
print(f'glass_2_2: occupied_volume - {glass_2_2. occupied_volume}')


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class GlassDefaultArg:
    """"
    Класс GlassDefaultArg это модель стакана c одним аргументом по умолчанию.
    Аттрибуты:
    capacity_volume - максимальный объем стакана
    occupied_volume - Текущий объем стакана
    """
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError


print('\n3. >')
glass_3_1 = GlassDefaultArg(200)
print(f'glass_3_1: capacity_volume - {glass_3_1. capacity_volume}')
print(f'glass_3_1: occupied_volume - {glass_3_1. occupied_volume}')

glass_3_2 = GlassDefaultArg(200, 200)
print(f'glass_3_2: capacity_volume - {glass_3_2. capacity_volume}')
print(f'glass_3_2: occupied_volume - {glass_3_2. occupied_volume}')


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?


class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        # occupied_volume = []       # как вариант, можно инициализировать переменную изменяемого типа
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


print('\n4. >')
glass_4_1 = GlassDefaultListArg(200)
print(f'glass_4_1: occupied_volume - {glass_4_1.occupied_volume}')            # [2]

glass_4_2 = GlassDefaultListArg(200)
print(f'glass_4_2: occupied_volume - {glass_4_2.occupied_volume}')            # [2, 2]

glass_4_3 = GlassDefaultListArg(200)
print(f'glass_4_3: occupied_volume - {glass_4_3.occupied_volume}')            # [2, 2, 2]

# Можно ли использовать для аргументов по умолчанию изменяемые типы? - Нельзя, т.к. экземпляры класса будут получать
# значения аргументов, измененных предыдущим экземпляром.


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.


class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if occupied_volume > capacity_volume:
            raise ValueError            # TODO проверить что количеситво жидкости не должно быть больше объема стакана

    def add_water(self, adding_water):
        space = self.capacity_volume - self.occupied_volume    # пустое место
        if adding_water > space:
            self.occupied_volume += space
            return print(f'недолитая вода - {adding_water-space}')       # недолитая вода
        else:
            self.occupied_volume += adding_water        # увеличиваем занятый объем  на объем  доливаемой воды

    def remove_water(self, removing_water):
        asd = self.occupied_volume - removing_water     # остаток в стакане
        if removing_water > self.occupied_volume:
            raise ValueError
        else:
            self.occupied_volume -= removing_water


print('\n5. >')

glass_5_1 = GlassAddRemove(200, 20)
print(f'glass_5_1: capacity_volume - {glass_5_1.capacity_volume}')
print(f'glass_5_1: occupied_volume - {glass_5_1.occupied_volume}')

glass_5_1.add_water(140)
print(f'занятый объем стакана после добавления- {glass_5_1.occupied_volume}')
glass_5_1.remove_water(150)
print(f'занятый объем стакана после удаления - {glass_5_1.occupied_volume}')


# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

print('\n6. >')

glass_6_1 = GlassAddRemove(200, 100)
glass_6_2 = GlassAddRemove(500, 50)
glass_6_3 = GlassAddRemove(100, 0)

print(f'Метод dir объекта glass_6_1:\n {dir(glass_6_1)}\n')
print(f'Метод dir объекта glass_6_2:\n {dir(glass_6_2)}\n')
print(f'Метод dir объекта glass_6_3:\n {dir(glass_6_3)}\n')
print(f'Метод dir класса GlassAddRemove:\n {dir(GlassAddRemove)}\n')

print(type(glass_6_1))
print(type(glass_6_2))
print(type(glass_6_3))
print(type(GlassAddRemove))

print(glass_6_1.__dict__)


# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__,
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.


class GlassDir:
    def __init__(self, capacity_volume, occupied_volume):
        print(f'список атрибутов экземпляра класса в начале метода __init_\n {dir(self)}')
        print(self.__dict__)
        self.capacity_volume = capacity_volume
        print(f'список атрибутов экземпляра класса в середине __init__\n {dir(self)}')
        print(self.__dict__)
        self.occupied_volume = occupied_volume
        print(f'список атрибутов экземпляра класса в конце __init__\n {dir(self)}')
        print(self.__dict__)

# с каждой инициализацией атрибут добавляется в список атрибутов класса

print('\n7. >')
glass_7_1 = GlassDir(200, 100)


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

print('\n8. >')
glass_8_1 = Glass(200, 100)
print(hex(id(glass_8_1)))
print(glass_8_1.get_self_id())       # метод создан в пункте 1

glass_8_2 = Glass(500, 50)
print(hex(id(glass_8_2)))
print(glass_8_2.get_self_id())      # метод создан в пункте 1

glass_8_3 = Glass(100, 0)
print(hex(id(glass_8_3)))
print(glass_8_3.get_self_id())      # метод создан в пункте 1


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)


print('\n9. >')
d.print_me(d())

#   корректно  - для интерпретатора Python;
#   некорректно - с точки зрениясоглашения о стиле кодирования


# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            # return  #  убрать return и вызвать raise error
            self.a = a
        else:
            raise ValueError


print('\n10. >')

a1 = A(20)
print(dir(a1))

a2 = A(2)
print(dir(a2))

# Объясните так реализовывать __init__ нельзя?
# return только для удачных условий. В случае невыполения условия лучше вызвать raise error.
# self определяется для удачных условий




# 11. Циклическая зависимость (стр. 39-44)
#
from weakref import ref


class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        return f'{self.__prev}{self.__next}'

    def __repr__(self):
        return f'Node: ({self.__prev},{self.__next})'


class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
        elif isinstance(nodes, Node):
            self.head = nodes
            self.tail = nodes
        elif isinstance(nodes, list):
            self.head = nodes[0]
            self.tail = nodes[-1]
            self.linken_nodes(nodes)     # связываем пользовательский набор узлов

    def linked_nodes(self, nodes):
        # установили ссылки для первого узла
        nodes[0].set_prev(nodes[-1])
        nodes[0].set_prev(nodes[1])

        # установили ссылки для середины
        for i in range(1, len(nodes) - 1):
            nodes[i].set_prev(nodes[i - 1])
            nodes[i].set_next(nodes[i + 1])
        # установили ссылки для последнего узла
        nodes[-1].set_prev(nodes[-2])       # TODO check when len of 1
        nodes[-1].set_prev(nodes[0])



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        self.tail.set_next(node)
        node.set_prev(self.tail)
        self.tail = node
        self.tail.set_next(self.head)
        self.head.set_next(self.tail)

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...



