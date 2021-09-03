"""
Модуль реализует библиотеку для хранения данных книг и поиск по каталогу.
"""
import json


class Book:
    def __init__(self, author=None, title=None, year=None ):
        self.__author = author
        self.__title = title
        self.__year = year

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
    def author(self, author):
        self.__author = author

    @title.setter
    def title(self, title):
        self.__title = title

    @year.setter
    def year(self, year):
        self.__year = year


class BookLib:
    def __init__(self, file_lib=None):

        self.__file_lib = file_lib

    @property
    def file_lib(self):
        return self.__file_lib

    @file_lib.setter
    def file_lib(self, file):
        self.__file_lib = file

    def add_del_book(self, book: Book, mode: str):
        """
        Функция добавления книги в библиотеку и удаления книги из библиотеки
        :param book:
        :param mode: команда (add - добавить, del - удалить)
        :return: True/False выполнена или не выполнена функция
        """
        this_book = {
            "Автор": book.author,
            "Название": book.title,
            "Год издания": book.year
        }
        function_result = False

        try:
            data = json.load(open(self.__file_lib, encoding="utf-8"))
        except FileNotFoundError:
            data = []
            if mode == 'add':
                data.append(this_book)
                function_result = True
        else:
            book_exist = False
            for books in data:
                if str(books["Автор"]) == book.author \
                        and str(books["Название"]) == book.title \
                        and str(books["Год издания"]) == book.year:
                    if mode == 'add':
                        print("Такая книга уже есть в библиотеке.")
                    book_exist = True
                    break
                else:
                    book_exist = False

            if book_exist is not True:
                if mode == 'add':
                    data.append(this_book)
                    function_result = True
            elif book_exist is True and mode == 'del':
                data.remove(this_book)
                function_result = True

        with open(self.__file_lib, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return function_result

    def search_book(self, text: str) -> list:
        """
        Функция поиска книги в библиотеке.
        :param text: строка поиска
        :return: список найденных книг
        """
        books_find = []
        try:
            data = json.load(open(self.__file_lib, encoding="utf-8"))
        except FileNotFoundError:
            print("Файл библиотеки не создан.")
        else:
            t = text.upper()
            for books in data:
                if (t in str.upper(books["Автор"])) \
                        or (t in str.upper(books["Название"]))\
                        or (t in str.upper(books["Год издания"])):
                    books_find.append(books)

        return books_find

    def edit_book(self, oldbook: Book, newbook: Book):
        """
        Функция редактирования информации о книге.
        :param oldbook: старая версия
        :param newbook: новая версия
        :return: True/False выполнена или не выполнена функция
        """
        if self.add_del_book(oldbook, 'del'):
            if self.add_del_book(newbook, 'add'):
                return True
            else:
                return False
        else:
            return False

    def run(self):
        """
        Функция реализует интерфейс взаимодействия с пользователем
        """
        print("Использовать библиотеку по умолчанию или создать новую?",
              '\n\t- yes (библиотка по умолчанию)', '\n\t- no (создать новую библиотеку)')
        file_lib = str(input("> "))
        if file_lib == 'yes' or file_lib == 'no':
            if file_lib == 'yes':
                self.__file_lib = "lib.txt"
            else:
                file = str(input('Введите путь библиотеки: >  '))
                self.__file_lib = file
        else:
            print('Некорректный ввод.', '\n')

        print('\n', 'Список допустимых команд:', '\n\t- add  --> Добавить книгу в библиотеку',
              '\n\t- del  --> Удалить книгу из библиотеку', '\n\t- edit --> Редактировать книгу',
              '\n\t- find --> Поиск книги', '\n\t- exit --> Выход', '\n')

        while True:
            command = str(input("Введите команду: > "))

            if command == 'add' or command == 'del' or command == 'edit' or command == 'find' or command == 'exit':
                if command == 'add':
                    newbook = Book()
                    newbook.author = str(input('Введите автора книги: >  '))
                    newbook.title = str(input('Введите название книги: >  '))
                    newbook.year = str(input('Введите год издания книги: >  '))
                    if self.add_del_book(newbook, 'add'):
                        print('> Книга добавлена', '\n')
                    else:
                        print('> Книга не добавлена', '\n')

                if command == 'del':
                    delbook = Book
                    del_author = str(input('Введите автора книги: >  '))
                    del_book_name = str(input('Введите название книги: >  '))
                    del_book_year = str(input('Введите год издания книги: >  '))
                    if self.add_del_book(delbook, 'del'):
                        print('> Книга удалена', '\n')
                    else:
                        print('> Книга не удалена', '\n')

                if command == 'edit':
                    oldnamebook = Book
                    newnamebook = Book
                    oldnamebook.author = str(input('Введите автора книги: >  '))
                    oldnamebook.title = str(input('Введите название книги: >  '))
                    oldnamebook.year = str(input('Введите год издания книги: >  '))
                    newnamebook.authorw = str(input('Введите нового автора книги: >  '))
                    newnamebook.title = str(input('Введите новое название книги: >  '))
                    newnamebook.year = str(input('Введите новый год издания книги: >  '))
                    if self.edit_book(oldnamebook, newnamebook):
                        print('> Книга отредактирована', '\n')
                    else:
                        print('> Книга не отредактирована', '\n')

                if command == 'find':
                    search_ = str(input('Введите поисковый запрос: >  '))
                    print('Список найденных книг: >  ', self.search_book(search_), '\n')

                if command == 'exit':
                    break
            else:
                print('Некорректный ввод.', '\nВедите комманду в соотвествии со списком команд.', '\n')


if __name__ == "__main__":

    booklib = BookLib("db.txt")
    booklib.run()
