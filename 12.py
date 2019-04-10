def test_func(*args):
    print(f"Тест с параметрами {args}")
    func = args[0]
    assert func(args[1]) == args[2], args[3]


def squared_foo(x):
    return x ** 2


if __name__ == '__main__':
    from sys import argv
    print(argv[1])
    if len(argv) > 1:
        filename, test_param1 = argv[0], argv[1]
        if (test_param1) != '--skiptest':

            if (test_param1) == 'half':
                print('Half')
                test_func(squared_foo, 2, 5, 'Квадрат числа 2')

                test_func(squared_foo, 2, 6, 'Квадрат числа 2')
            else:
                print('All tests')
                test_func(squared_foo, 2, 5, 'Квадрат числа 2')

                test_func(squared_foo, 2, 6, 'Квадрат числа 2')
                test_func(squared_foo, 2, 4, 'Квадрат числа 2')

                test_func(squared_foo, 2, 4, 'Квадрат числа 2')
        else:
            print('Тесты не запускаются')