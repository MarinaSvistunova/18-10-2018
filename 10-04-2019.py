"""
Главный запускаемый файл приложения

"""

class User():
    """Посетитель библиотеки"""
    pass

    def __init__(self, first_name, second_name, date_of_birth, passport_number):

        self.passport_number = passport_number
        self.first_name = first_name
        self.second_name = second_name
        self.date_of_birth = date_of_birth

    def get_user_info(self):
        info = f"№ паспорта: {self.passport_number}\n" \
               f"Фамилия имя: {self.second_name} {self.first_name}"

        return info


class Book():
    """Книга, с которой будет работать посетитель в библиотеке"""
    pass


def main():
    new_user = User('Seok-Jin', 'Kim', '4-12-1992', '12 34 567890')
    info = new_user.get_user_info()
    print(info)


if __name__ == '__main__':
    print("Запустить тесты")
    app = main()