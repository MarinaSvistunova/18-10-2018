def Discriminant(a=0, b=0, c=0):
    return b * b - 4 * a * c


def Eql(a=0, b=0, c=0, accuracy=0):
    """
        Функция
    """
    D = Discriminant(a, b, c)
    if accuracy > 0.00001:
        accuracy = int(len((str(accuracy))[2::]))
    else:
        accuracy = int(str(accuracy)[3::])
    if D > 0:
        sD = D ** (1 / 2)
        x1 = float('{0:.{w}f}'.format((-b + sD) / (2 * a), w=accuracy))
        x2 = float('{0:.{w}f}'.format((-b - sD) / (2 * a), w=accuracy))
        return [x1, x2]
    elif D == 0 and a != 0:
        return float('{0:.{w}f}'.format((-b) / (2 * a), w=accuracy))
    else:
        return -1


def test_assert(*args):
    """
        args = (func, *operands, exp_value, "Failed assertion message")
    """
    func, *operands, exp_value, er = args[0], *args[1:-2], args[-2], args[-1]
    try:
        assert func(
            *operands) == exp_value, f"Failed assertion message with func {func}{operands}, exp value is {exp_value}"
    except AssertionError as e:
        print(e)

'''
def test_assert(*args):
    """
        args = (func, *operands, exp_value, "Failed assertion message")
    """
    func, *operands, exp_value, er = args[0], *args[1:-2], args[-2], args[-1]
    try:
        assert func(
            *operands) == exp_value, f"Failed assertion message with func {func}{operands}, exp value is {exp_value}"
        return 1
    except AssertionError as e:
        print(e)
        return 2
        

# print(Eql(4,4,1,0.1))
def test_case():
    S = []
    F = []
    el = [[Eql, 5, 8, -2, 0.001, [0.2, -2.0], "el"], [Eql, 4, 4, 1, 0.1, 0.5, "i"],
          [Eql, 5, 9, -2, 0.001, [0.2, -2.0], "u"]]
    for i in el:
        a = test_assert(*i)
        i[0] = i[0].__name__
        if a == 1:
            S += [i]
        elif a == 2:
            F += [i]
        print("\n")
    print("S: ", S, "\nF: ", F)
    print("Успешно: ", len(S), "\nПровалено: ", len(F))


test_case()

# test_assert(Eql,5,9,-2,0.001,[0.2,-2.0])
# test_assert(Eql,5,8,-2,0.001,[0.2,-2.0])
# test_assert(Eql,4,4,1,0.1,-0.5)
'''

if __name__ == '__main__':
    from sys import argv

    el = [[Eql, 5, 8, -2, 0.001, [0.2, -2.0], "el"], [Eql, 4, 4, 1, 0.1, 0.5, "i"],
          [Eql, 5, 9, -2, 0.001, [0.2, -2.0], "u"]]

    if len(argv) > 1:
        '''filename, test_param1 = argv[0], argv[1]
        if (test_param1) != '--skiptest':
            if (test_param1) == '0':
                d[0]
        else:
            print('Тесты не запускаются')'''
        print(argv)
        if '--t' in argv:
            print('Указан ключ для запуска тестов')

            # Должна быть возможность запуска отдельных тестов
            # с помощью ключа t=<индентификатор теста>
            # python cl-run-tests.py test=2,3,4,5,6
            # python cl-run-tests.py --random
        k = argv[1].find('test=')
        if k != -1:
            arguments = []
            for arg in argv:
                if '=' in arg:
                    a, v = arg.split('=')
                    arguments.append(int(v))
                    test_assert(*(el[int(v)]))

        if '--d' in argv:
            arguments = []
            # python cl-run-tests.py a=4 exp_val=16 --d
            # python cl-run-tests.py --d a=4 exp_val=16
            # python cl-run-tests.py --d a=10 exp_val=100
            for arg in argv:
                if '=' in arg:
                    a, v = arg.split('=')
                    arguments.append(int(v))

            print(arguments)
            test_func(squared_foo, arguments[0], arguments[1], "some_text_error")
