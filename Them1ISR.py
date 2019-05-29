# Свистунова Марина, 2ИВТ(1.2)
# Задание 4.1 - 4.4
''' 4.1. Разработать программу для считывания данных JSON-формата из файла и вывод их в табличном виде на экран.
         Организовать тестирование работоспособности программы с помощью assert, print.
         Список исключительных ситуаций, которые могут возникнуть:
         * отсутствие модуля json и/или pprint  (ImportError);
         * отсутствие файла (FileNotFoundError);
         * ошибка в структуре JSON, включая отсутствие содержимого файла (JSONDecodeError);
         * в каких ситуациях может возникнуть IOError?
         * KeyError и/или IndexError в случае непрофессионального итерирования по объекту, взятия значений по ключам;
         * подумать, есть ли ещё?
    4.2. Дополнение программы задания 4.1 (считывание данных JSON-формата) тестами с использованием библиотеки doctest.
    4.3. Дополнение программы задания 4.1,4.2 (считывание данных JSON-формата) тестами с использованием пакета py.test.
    4.4. Формирование отчета по самостоятельно работе и публикация его в портфолио. '''

def my_print(line = []):
    """
    Функция вывода таблицы
    В функцию передается массив, состоящий из ключа и значений, каждый из
    которых является массивом. Каждый массив, переданного массива,
    состоит из одинакогово количества элементов.
    В функции составляется в цикле новый массив, состоящий из i-ых значений
    каждого начального массива. Затем созданный массив выводится в виде строки
    таблицы.
    """
    lenCol = 30
    for i in range(len(line[0])):
        newArray = []
        for i2 in range(len(line)):
            newArray += [line[i2][i]]
        for i3 in range(len(newArray)):
            print(newArray[i3].ljust(lenCol,' '), end = "")
            print("|", end = "")
        print()
    print('-'*(lenCol + 1)*len(line))

def changeStr(str = ''):
    """
    Функция деления строки
    В функцию передается строка. Производится проверка ее длины, если длина
    переданной строки больше заданного числа, то строка делится, а
    соответствующие части записываются в массив. Если длина строки меньше или
    равна заданному числу, то функция возвращается массив, элементом которого
    является изначальная строка.
    """
    lenStr = 30
    arrayStr = []
    if len(str) > lenStr:
        i = 0
        while i <= len(str):
            arrayStr += [str[i:i+lenStr]]
            i += lenStr
        return arrayStr
    else:
        return [str]

def addArray(array = []):
    """
    Функция для корректировки колличества элементов массива
    В функцию передается массив из массивов. Считаются минимальное и
    максимальное значения длин массивов. Если минимальное и максимальное
    значения не равны, то каждый внутренний массив дополняется необходимым
    количеством элементов. Иначе возвращается изначальный массив.
    """
    if type(array[0][0]) == str:
        min = len(array[0])
        max = 0
        for i in array:
            if len(i) > max:
                max = len(i)
            elif len(i) < min:
                min = len(i)
        if min != max:
            for i in range(len(array)):
                if len(array[i]) < max:
                    for k in range(max-min):
                        array[i] += ['']
    elif type(array[0]) == list:
        for i in range(len(array)):
            array[i] = addArray(array[i])
    return array

def listKeys(dictList):
    """
    Функция для выделения ключей словаря в массив
    В функцию передаются ключи словаря.
    """
    keyList = []
    for key in dictList:
        keyList += [key]
    return keyList

# import pytest
# def test_digit(string):
#     with pytest.raises(ValueError):
#         int(string)

def is_digit(string):
    """
    Функция для определения является ли переданное значение числом
    В функцию передается строка.
    """
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def testingType(line):
    """
    Функция для опрделения типа переданного значения и переделывание его в
    строку/массив
    В функцию передается значение неопределенного типа.
    """
    # если значение - логический тип
    if is_digit(str(line)) == True:
        return str(line)
    else:
        if line == True:
            line = 'Yes'
            return line
        elif line == False:
            line = 'No'
            return line

    # если значение - список или  кортеж или множество
    if isinstance(line, (list, tuple, set)):
        if type(line[0]) == dict:
            newList = []
            for each in line:
                newList += [testingType(each)]
            line = newList
            return line
        else:
            line = [str(i) for i in line]
            return line

    # если значение - словарь
    if type(line) == dict:
        keyDict = listKeys(line)
        newVal = []
        for each in keyDict:
            newVal += [testingType(line.get(each))]
        line = newVal

    return(line)

def changeArr(line):
    """
    Функция для преобразование массива с вложенными массивами
    В функцию передается массив из массивов. Функция возвращает массив,
    упрощенный на один уровень.
    """
    arr = []
    for i in range(len(line)):
        arr += line[i]
    return arr

def readFile():
    """
    Функция для считывания json
    В функции преобразуется исходный файл к виду, удобному для вывода в виде
    таблицы.
    """
    #считывание файла
    try:
        fileName = 'data.json'
        fileOpen = open(fileName)
        try:
            import json
        except ImportError as e:
            import json
            print("Problem with import json")
        data = json.load(fileOpen)
        #список всех ключей
        keyList = listKeys(data[0].keys())
        # преобразование файла
        for eachPart in data:
            for key in keyList:
                eachPart[key] = testingType(eachPart[key])
                if type(eachPart[key]) == str:
                    eachPart[key] = changeStr(eachPart[key])
                elif type(eachPart[key]) == list:
                    for i in range(len(eachPart[key])):
                        if type(eachPart[key][i]) == list:
                            for i2 in range(len(eachPart[key][i])):
                                eachPart[key][i][i2] = changeStr(eachPart[key][i][i2])
                        else:
                            [eachPart[key][i]] = changeStr(eachPart[key][i])

        for eachKey in keyList:
            array = [[eachKey]]
            for eachPart in data:
                if type(eachPart[eachKey][0]) == list:
                    while (type(eachPart[eachKey][0]) != str):
                        eachPart[eachKey] = changeArr(eachPart[eachKey])
                array += [eachPart[eachKey]]
            my_print(addArray(array))

    except FileNotFoundError as e:
        print("File not found")
    except IOError as e:
        print("Problem with input or output")
    except (KeyError, IndexError) as e:
        print("Problem with keys or indexes")

readFile()

import functools
def test_assert(*args):
    """
        args = (func, *operands, exp_value, "Failed assertion message")
    """
    func, *operands, exp_value, er = args[0], *args[1:-2], args[-2], args[-1]
    try:
        assert func(*operands) == exp_value, f"Failed assertion message with func {func}{operands}, exp value is {exp_value}"
    except AssertionError as e:
        print(e)

if __name__ == '__main__':
    '''
    python Them1ISR.py test=0  - запуск любого теста из списка, вместо 0 любое число
    python Them1ISR.py test=-1 - запуск всех тестов
    '''
    from sys import argv
    el = [[testingType, 56, '56', "1"], [testingType, True, 'Yes', "2"],
          [testingType, (5, 6, 7), [5, 6, 7], "3"]]

    if len(argv) > 1:
        print(argv)
        k = argv[1].find('test=')
        if k != -1:
            arguments = []
            for arg in argv:
                if '=' in arg:
                    a, v = arg.split('=')
                    arguments.append(int(v))
                    test_assert(*(el[int(v)]))
        if k == -1:
            for i in range(len(el)):
                test_assert(*(el[i]))
