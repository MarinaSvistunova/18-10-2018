def unique_func(*args):
    ''' Функция возвращает список уникальных элементов из переданных в функцию
        Элементы преобразовываются в словарь, в основную функцию передаются keys словаря '''
    d = {}
    for i in args:
        if isinstance(i, (list, tuple)):
            d.update(zip(i, i))
        else:
            d.update({i: i})
    return list(d.keys())


print(unique_func([2, 3, 5, 5, 6, 3, 5]))
print(unique_func([1, 2, 23456, 23456, 234567, 234567, 'a', 1.6], 8, 7, 's'))
print(unique_func([1], 3, ['s', 'd', 6, 5, 7, 's']))
print(unique_func([1], ('a', 4, 5), 'f', 3, ['s', 'd', 6, 5, 7, 's']))

if __name__ == '__main__':
    assert type(unique_func([1, 4, 5, 5, 5, 3, 77, 4])) == list, "Тип"
    assert unique_func([1, 4, 5, 5, 5, 3, 77, 4]) == [1, 4, 5, 3, 77], "Целые числа"
    assert unique_func([1, 3, 's'], 'd', 6, 5, 7, 's') == [1, 3, 's', 'd', 6, 5, 7], "Список и произвольные аргументы"
    assert unique_func([1, 4, 5, 5, 5, 3, 77, 4]) == [1, 4, 5, 3, 77], "Произвольные аргументы"
    assert unique_func([1, 3, 's'], ('d', 6, 5, 7, 's')) == [1, 3, 's', 'd', 6, 5, 7], "Список и кортеж"
    assert unique_func((1, 4, 5, 5, 5, 3, 77, 4)) == [1, 4, 5, 3, 77], "Кортеж"
    assert unique_func((1, 3, 4), 'd', (6, 5, 7), ('s')) == [1, 3, 4, 'd', 6, 5, 7, 's'], "Кортежи и произвольный элемент"
    assert unique_func([1, 4, 5, 5, 5, 3, 77, 4], [1, 4, 5, 5, 5, 3, 77, 4]) == [1, 4, 5, 3, 77], "Два одинаковых списка"
    assert unique_func('f', [1, 4, 5, 5, 5, 3, 77, 4]) == ['f', 1, 4, 5, 3, 77], "Произвольный элемент и список"
    assert unique_func('f', (1, 4, 5, 5, 5, 3, 77, 4)) == ['f', 1, 4, 5, 3, 77], "Произвольный элемент и кортеж"




