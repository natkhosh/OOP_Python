# Лабораторная работа № 1.2
# Слушатель (ФИО): Мокрушина Н.Ю.


#TODO
# + 1. Реализовать класс Date согласно шаблону
#     1.1 Конструктор класса
#     1.2 Свойства для дня, месяца, года
#     1.3 Сеттеры и геттеры для свойств
# + 2. Реализовать методы add_day, add_month, add_year
# 3. Переопределить магические методы для класса Date:
#    + __lt__(self, other) - x < y вызывает x.__lt__(y).
#    + __le__(self, other) - x ≤ y вызывает x.__le__(y).
#    + __eq__(self, other) - x == y вызывает x.__eq__(y).
#    + __ne__(self, other) - x != y вызывает x.__ne__(y).
#    + __gt__(self, other) - x > y вызывает x.__gt__(y).
#    + __ge__(self, other) - x ≥ y вызывает x.__ge__(y).
# 4. Перегрузка арифметических операторов для класса Date:
#    + __add__(self, other) - сложение. x + y вызывает x.__add__(y).
#    + __sub__(self, other) - вычитание (x - y).
#    + __radd__(self, other).
#    + __rsub__(self, other).
#    + __iadd__(self, other) - +=.
#    + __isub__(self, other) - -=.
# + 5. Переопределить преобразование типа в int.
#     __int__(self)
# + 6. Перегрузить конструктор класса
# 7. Написать тесты для проверки реализованного функционала (Необязательное)

import datetime
from datetime import date


class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

    def __init__(self, *args):
        """Examples:
            Format: year, month, day
            d1 = Date(2020, 2, 20)      # 20.2.2020
            d2 = Date()                 # current date
            d3 = Date(2020)             # current date
        """
        if len(args) >= 3:
            self.is_valid_date(args[0], args[1], args[2])
            self.__year = args[0]
            self.__month = args[1]
            self.__day = args[2]
        else:
            now = datetime.datetime.now()
            self.__year = now.year
            self.__month = now.month
            self.__day = now.day

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    def __int__(self):
        """  Override conversion type to int
        Example:
            date2 = Date(2020, 1, 12) --> 737985
        :return: days: int --> number of days
        """
        print(f'Дата >  {self.__str__()}')
        days = ((self.__year // 3) * 366) + ((self.__year - (self.__year // 3)) * 365)
        for i in range(1, self.__month):
            days += self.get_max_day(self.__year, i)
        days += self.__day
        print(f'Дней: {days}')
        return days

    def __lt__(self, other):
        """ __lt__(self, other) --> x < y
        вызывает x.__lt__(y)
        :param other:
        :return: True or False
        """
        if self.__year < other.year:
            return True
        elif self.__year > other.year:
            return False
        else:
            if self.__month < other.month:
                return True
            elif self.__month > other.month:
                return False
            else:
                if self.__day < other.day:
                    return True
                elif self.__day >= other.day:
                    return False

    def __le__(self, other):
        """ __le__(self, other) --> x ≤ y
        вызывает x.__le__(y)
        :param other:
        :return: True or False
        """
        if self.__year <= other.year:
            return True
        elif self.__year > other.year:
            return False
        else:
            if self.__month <= other.month:
                return True
            elif self.__month > other.month:
                return False
            else:
                if self.__day <= other.day:
                    return True
                elif self.__day > other.day:
                    return False

    def __eq__(self, other):
        """ __eq__(self, other) --> x == y
        вызывает x.__eq__(y)
        :param other:
        :return: True or False
        """
        if (self.__day == other.day) and (self.__month == other.month) and (self.__year == other.year):
            return True
        else:
            return False

    def __ne__(self, other):
        """ __ne__(self, other) --> x != y
        вызывает x.__ne__(y)
        :param other:
        :return: True or False
        """
        if (self.__day != other.day) or (self.__month != other.month) or (self.__year != other.year):
            return True
        else:
            return False

    def __gt__(self, other):
        """ __gt__(self, other) --> x > y
        вызывает x.__gt__(y)
        :param other:
        :return: True or False
        """
        if self.__year > other.year:
            return True
        elif self.__year < other.year:
            return False
        else:
            if self.__month > other.month:
                return True
            elif self.__month < other.month:
                return False
            else:
                if self.__day > other.day:
                    return True
                elif self.__day <= other.day:
                    return False

    def __ge__(self, other):
        """ __ge__(self, other) --> x ≥ y
        вызывает x.__ge__(y)
        :param other:
        :return: True or False
        """
        if self.__year >= other.year:
            return True
        elif self.__year < other.year:
            return False
        else:
            if self.__month >= other.month:
                return True
            elif self.__month < other.month:
                return False
            else:
                if self.__day >= other.day:
                    return True
                elif self.__day < other.day:
                    return False

    def __add__(self, other):
        """ __add__(self, other) --> x + y
        вызывает x.__add__(y)
        Example:
            d1 = Date(2020, 1, 20)
            d1 + 11                # Полученная дата > 31.1.2020
        :param other: int
        """
        if not isinstance(other, int):
            raise ValueError
        elif other < 0:
            raise ValueError('Date must be positive')
        else:
            self.add_day(other)
            return self

    def __radd__(self, other):
        """ __add__(self, other) --> y + x
            вызывает y.__radd__(x)
            Example:
                d2 = Date(2020, 1, 20)
                11 + d2                # Полученная дата > 31.1.2020
            :param other: int
            """
        if not isinstance(other, int):
            raise ValueError
        elif other < 0:
            raise ValueError('Date must be positive')
        else:
            self.add_day(other)
            return self

    def __sub__(self, other):
        """"
        __sub__(self, other) --> x - y
            вызывает x.__sub__(y)
            Example:
                date_2 = Date(2020, 1, 1)
                date_2 - 5                # Полученная дата > 28.12.2019
            :param other: int
        """
        if not isinstance(other, int):
            raise ValueError
        elif other < 0:
            raise ValueError('Date must be positive')
        else:
            x = other - self.__day
            if x < 0:
                self.__day -= other
            elif x == 0:
                self.__day = 1
            else:
                self.__month = self.__month - 1
                if self.__month == 0:
                    self.__month = 12
                    self.__year = self.__year - 1
                    self.__day = self.get_max_day(self.__year, self.__month)
                else:
                    self.__day = self.get_max_day(self.__year, self.__month)

                if x < self.get_max_day(self.__year, self.__month):
                    self.__day = self.get_max_day(self.__year, self.__month) - x + 1
                elif x == 0:
                    self.__day = self.get_max_day(self.__year, self.__month) - x + 1
                else:
                    self.__sub__(x)
            return self

    def __rsub__(self, other):
        """"
        __rsub__(self, other) --> y - x
            вызывает y.__sub__(x)
            Example:
                date_2 = Date(2019, 12, 28)
                30 - date_2                # Полученная дата > 29.11.2019
            :param other: int
        """
        if not isinstance(other, int):
            raise ValueError
        elif other < 0:
            raise ValueError('Date must be positive')
        else:
            x = other - self.__day
            if x < 0:
                self.__day -= other
            elif x == 0:
                self.__day = 1
            else:
                self.__month = self.__month - 1
                if self.__month == 0:
                    self.__month = 12
                    self.__year = self.__year - 1
                    self.__day = self.get_max_day(self.__year, self.__month)
                else:
                    self.__day = self.get_max_day(self.__year, self.__month)

                if x < self.get_max_day(self.__year, self.__month):
                    self.__day = self.get_max_day(self.__year, self.__month) - x + 1
                elif x == 0:
                    self.__day = self.get_max_day(self.__year, self.__month) - x + 1
                else:
                    self.__rsub__(x)
            return self

    def __iadd__(self, other):
        """"
        __iadd__(self, other) -->   +=
            вызывает x.__iadd__(y)
            Example:
                date = Date(2020, 1, 1)
                date += 15                # Полученная дата > 16.1.2020
            :param other: int
        """
        if not isinstance(other, int):
            raise ValueError
        elif other < 0:
            raise ValueError('Date must be positive')
        else:
            self.__add__(other)
            return self

    def __isub__(self, other):
        """"
       __isub__(self, other) -->   -=
            вызывает x.__isub__(y)
            Example:
                date = Date(2020, 1, 16)
                date -= 10                # Полученная дата > 1.1.2020
            :param other: int
        """
        if not isinstance(other, int):
            raise ValueError
        elif other < 0:
            raise ValueError('Date must be positive')
        else:
            self.__sub__(other)
            return self

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            return True
        else:
            return False

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @day.setter
    def day(self, value):
        value = int(value)
        self.is_valid_date(self.__year, self.__month, value)
        self.__day = value

    @month.setter
    def month(self, value):
        value = int(value)
        self.is_valid_date(self.__year, value, self.__day)
        self.__month = value

    @year.setter
    def year(self, value):
        value = int(value)
        self.is_valid_date(value, self.__month, self.__day)
        self.__year = value

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    def add_year(self, year):
        if not isinstance(year, int):
            raise TypeError('Date must be integer')
        if year < 0:
            raise ValueError('Invalid date format. Date must be positive')
        self.__year += year
        return self.__year

    def add_month(self, month):
        if not isinstance(month, int):
            raise TypeError('Date must be integer')
        if month < 0:
            raise ValueError('Invalid date format. Date must be positive')
        months = self.__month + month
        if months > 12:
            self.__month = months % 12
            self.add_year(int(months // 12))
            return self.__month
        else:
            self.__month += month
            return self.__month

    def add_day(self, day):
        if not isinstance(day, int):
            raise TypeError('Date must be integer')
        if day < 0:
            raise ValueError('Invalid date format. Date must be positive')
        days = self.__day + day
        if days > self.get_max_day(self.__year, self.__month):
            days -= self.get_max_day(self.__year, self.__month)
            self.add_month(1)
            self.__day = 0
            self.add_day(days)
        else:
            self.__day = days
            return self.__day

    @staticmethod
    def date2_date1(date2, date1):
        if date2 < date1:
            raise ValueError
        else:
            days_diff = date2.__int__() - date1.__int__()
            print(f'Разница дней: {days_diff}')


if __name__ == "__main__":
    date_my = Date(2020, 4, 12)

    date_my.date = '25.11.2015'
    print(date_my.date)

    print(f'{date_my.__dict__}\n')

    date_my.day = 9
    date_my.month = 4
    date_my.year = 1980
    print(f'Birthday date: {date_my.__str__()}''\n')

    date_s = Date(2011, 8, 10)
    date_s._Date__day = 22
    print(f'New date: {date_s.__str__()}''\n')

    print(f'Перевод даты в дни: ''\n'
          f'Число дней: {date_my.__int__()}''\n')

    d1 = Date(2020, 3, 1)
    d1.add_day(30)
    d1.add_month(13)
    d1.add_year(5)
    print(d1.date)

    date1 = Date(2020, 1, 22)
    date2 = Date(2020, 2, 12)

    print('----\n Method > date2_date1')
    dateSub = Date.date2_date1(date2, date1)

    print('----\nПеревод даты в дни -->')
    date1.__int__()
    date2.__int__()

    print('\nПерегрузка __init__ -->  current date')
    d3 = Date()
    print(d3)

    print('----\n Method > __lt__')
    print(date1 < date2)

    date_1 = Date(2020, 1, 1)
    print('----\n Method > __add__')
    100 + date_1

    print('----\n Method > __radd__')
    date_1 + 15

    # print('----\n Method > __sub__')
    # date_2 = Date(2020, 1, 1)
    # print(date_2 - 5)

    # print('----\n Method > __rsub__')
    # print(f'{30 - date_2}')

    print('----\n Method > __iadd__')
    date_3 = Date(2020, 1, 1)
    date_3 += 15

    print('----\n Method > __isub__')
    date_4 = Date(2020, 1, 16)
    date_4 -= 15
    print('--------------')
    date = Date(2020, 1, 1)

    print(date + 5)

    print('----\n Method > __sub__')
    date_2 = Date(2020, 1, 1)
    print(date_2 - 5)

    print('----\n Method > __rsub__')
    print("sdklfj", 30 - date_2)