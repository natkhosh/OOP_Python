from structure_driver import *
from builder import *
from react import *
from LinkedList import *


class Book(WeakSubject):
    def __init__(self, author, title, year):
        super().__init__()
        self.is_valid_book(author, title, year)
        self.__author = author
        self.__title = title
        self.__year = year

    def __str__(self):
        return f'{self.__author} {self.__title} {self.__year}'

    @classmethod
    def is_valid_book(cls, author, title, year):
        if not isinstance(author, str):
            raise TypeError('author must be string')
        if not isinstance(title, str):
            raise TypeError('title must be string')
        if not isinstance(year, str):
            raise TypeError('year must be string')

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, name):
        name = str(name)
        self.is_valid_book(name, self.__title, self.__year)
        self.__author = name
        self.notify()

    @title.setter
    def title(self, value):
        value = str(value)
        self.is_valid_book(self.__author, value, self.__year)
        self.__title = value
        self.notify()

    @year.setter
    def year(self, value):
        value = str(value)
        self.is_valid_book(self.__author, self.__title, value)
        self.__year = value
        self.notify()


class Library:

    def __init__(self):
        self.__ll = None
        # self.__structure_driver = structure_driver

    def __init_drivers(self):
        driver_name = input("Введите название драйвера > ")
        structure_driver = SDFabric.get_sd_driver(driver_name).build()
        self.__ll = LinkedList(structure_driver)

    def main(self):
        self.__init_drivers()

        print("Использовать библиотеку по умолчанию или создать новую?",
              '\n\t- yes (библиотка поумолчанию)', '\n\t- no (создать новую библиотеку)')
        file_lib = str(input("> "))

        if file_lib == 'yes' or file_lib == 'no':
            if file_lib == 'yes':
                file = "library_02.txt"

            else:
                file = str(input('Введите путь библиотеки: >  '))
        else:
            print('Некорректный ввод.', '\n')

        print('\n', 'Список допустимых команд:', '\n\t- add  --> Добавить книгу в библиотеку',
              '\n\t- del  --> Удалить книгу из библиотеку', '\n\t- edit --> Редактировать книгу',
              '\n\t- find --> Поиск книги', '\n\t- exit --> Выход', '\n')
        while True:
            command = str(input("Введите команду: > "))

            if command == 'add' or command == 'del' or command == 'edit' or command == 'find' or command == 'exit':
                if command == 'add':
                    add_author = str(input('Введите автора книги: >  '))
                    add_book_name = str(input('Введите название книги: >  '))
                    add_book_year = str(input('Введите год издания книги: >  '))
                    if add_del_book(file, add_author, add_book_name, add_book_year, 'add'):
                        print('> Книга добавлена', '\n')
                    else:
                        print('> Книга не добавлена', '\n')

                if command == 'del':
                    del_author = str(input('Введите автора книги: >  '))
                    del_book_name = str(input('Введите название книги: >  '))
                    del_book_year = str(input('Введите год издания книги: >  '))
                    # if add_del_book(file, del_author, del_book_name, del_book_year, 'del'):
                    #     print('> Книга удалена', '\n')
                    # else:
                    #     print('> Книга не удалена', '\n')

                if command == 'edit':
                    add_author = str(input('Введите автора книги: >  '))
                    add_book_name = str(input('Введите название книги: >  '))
                    add_book_year = str(input('Введите год издания книги: >  '))
                    add_author_new = str(input('Введите нового автора книги: >  '))
                    add_book_name_new = str(input('Введите новое название книги: >  '))
                    add_book_year_new = str(input('Введите новый год издания книги: >  '))
                    # if edit_book(file, add_author, add_book_name, add_book_year, add_author_new, add_book_name_new,
                    #              add_book_year_new):
                    #     print('> Книга отредактирована', '\n')
                    # else:
                    #     print('> Книга не отредактирована', '\n')

                if command == 'find':
                    search_ = str(input('Введите поисковый запрос: >  '))
                    # print('Список найденных книг: >  ', search_book(file, search_), '\n')

                if command == 'exit':
                    break
            else:
                print('Некорректный ввод.', '\nВедите комманду в соотвествии со списком команд.', '\n')

    def add_del_book(Book, mode):
        """
        Функция добавления книги в библиотеку и удаления книги из библиотеки

        :param file: путь к файлу библиотки
        :param author: автор книги
        :param title: название книги
        :param year: год издания
        :param mode: команда (add - добавить, del - удалить)
        :return: True/False выполнена или не выполнена функция
        """
        book = {
            "Автор": Book.author,
            "Название": Book.title,
            "Год издания": Book.year
        }
        function_result = False

        try:
            data = json.load(open(file, encoding="utf-8"))
        except FileNotFoundError:
            data = []
            if mode == 'add':
                data.append(book)
                function_result = True
        else:
            book_exist = False
            for books in data:
                if str(books["Автор"]) == author and str(books["Название"]) == title and str(
                        books["Год издания"]) == year:
                    if mode == 'add':
                        print("Такая книга уже есть в библиотеке.")
                    book_exist = True
                    break
                else:
                    book_exist = False

            if book_exist is not True:
                if mode == 'add':
                    data.append(book)
                    function_result = True
            elif book_exist is True and mode == 'del':
                data.remove(book)
                function_result = True

        with open(file, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return function_result




