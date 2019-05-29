"""
Главный запускаемый файл приложения

"""
import sqlite3

class User():
    """Посетитель библиотеки"""

    def __init__(self, first_name, second_name, date_of_birth, passport_number):

        self.connectDB = sqlite3.connect('library.db')
        self.cursor = self.connectDB.cursor()
        self.create_lib(self.cursor)

        self.passport_number = passport_number
        self.first_name = str(first_name)
        self.second_name = second_name
        self.date_of_birth = date_of_birth

        self.insert_data(self.cursor)

    def get_user_info(self):
        info = f"№ паспорта: {self.passport_number}\n" \
               f"Фамилия имя: {self.second_name} {self.first_name}"

        return info

    def create_lib(self, cursor):
            cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
            'Passport_number' TEXT,
            'First_name' TEXT,
            'Second_name' TEXT,
            'Date_of_birth' TEXT) """)
           # self.connectDB.commit()
    # 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

    def insert_data(self, cursor):
        new_wr = [self.passport_number, self.first_name, self.second_name, self.date_of_birth]
        cursor.execute("INSERT INTO Users VALUES (?,?,?,?)", new_wr)
        self.connectDB.commit()


class Book():
    """Книга, с которой будет работать посетитель в библиотеке"""
    def __init__(self, book_name, book_author, book_year, book_number):
        self.connectDB = sqlite3.connect('library.db')
        self.cursor = self.connectDB.cursor()
        self.create_book(self.cursor)

        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
        self.book_number = book_number

        self.insert_data(self.cursor)


    # def get_user_info(self):
    #     info = f"№ паспорта: {self.passport_number}\n" \
    #            f"Фамилия имя: {self.second_name} {self.first_name}"
    #
    #     return info

    def create_book(self, cursor):
            cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            'Book_name' TEXT,
            'Book_author' TEXT,
            'Book_year' TEXT,
            'Book_number' TEXT) """)
           # self.connectDB.commit()
    # 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

    def insert_data(self, cursor):
        new_wr = [None, self.book_name, self.book_author, self.book_year, self.book_number]
        cursor.execute("INSERT INTO Books VALUES (?,?,?,?,?)", new_wr)
        self.connectDB.commit()


class Library_card():
    def __init__(self, id_user, id_book):
        # action - оформить книгу, добавить книгу, удалить книгу
        self.connectDB = sqlite3.connect('library.db')
        self.cursor = self.connectDB.cursor()
        self.create_library_card(self.cursor)

        self.id_user = id_user
        self.id_book = id_book


    def create_library_card(self, cursor):
        cursor.execute("""CREATE TABLE IF NOT EXISTS Cards (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        'id_user' TEXT NOT NULL,
        'id_book' INTEGER NOT NULL) """)

    def insert_data(self, cursor):
        new_wr = [None, self.id_user, self.id_book]
        cursor.execute("INSERT INTO Cards VALUES (?,?,?)", new_wr)
        self.connectDB.commit()

    def delete_data(self, cursor):
        new_wr = [None, self.id_user, self.id_book]
        cursor.execute("DELETE FROM Cards WHERE 'id_user'==VALUES (?) and 'id_book'==VALUES (?)", new_wr[1], new_wr[2])
        self.connectDB.commit()


def main():
    # new_user = User('Seok-Jin', 'Kim', '4-12-1992', '1234567890')
    # new_user2 = Book('Book about BTS', 'Kim N.', '2018', '30000')
    # info = new_user.get_user_info()

    # new_card=Library_card('12344563', '324325')
    new_card = Library_card.insert_data('1233265663', '324325')
    # del_card = Library_card.de
    # print(info)


if __name__ == '__main__':
    print("Запустить тесты")
    app = main()