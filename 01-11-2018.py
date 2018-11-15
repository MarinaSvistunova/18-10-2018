# Свистунова Марина, 2ИВТ
# 01.11.2018, Лабораторная работа

def unique_func(iterable, seen=list()): #seen = None
    # Функция возвращает список уникальных элементов
    if len(seen) == 0:   #seen = list(seen or [])
        seen = list()
    for item in iterable:
        if item not in seen:
            seen.append(item)
    return list(seen)

print(unique_func([1, 1, 2, 27, 3, 3]))
print(unique_func([1, 1, 2, 3, 3], seen = [2, 9]))

#print(unique_func([1, 1, 2, 3, 3], seen = unique_func([3, 3, 9])))


def unique_func2(*iterable, seen = []):
    # Функция возвращает список уникальных элементов. В функцию может быть передано различное количество элементов
    if len(seen) == 0:
        seen = list()
    for item in iterable:
        if type(item) == list:
            for item2 in item:
                if item2 not in seen:
                    seen.append(item2)
        else:
            if item not in seen:
                seen.append(item)
    return list(seen)

print(unique_func2([1, 1, 2, 27, 3, 3], [6, 1], 7, 's', 'f', seen = [4]))

if __name__ == '__main__':
    assert type(unique_func2([1, 4, 5, 5, 5, 3, 77, 4], seen =[3, 8])) == list, "Тип"
    assert unique_func2([1, 4, 5, 5, 5, 3, 77, 4], seen =[3, 8]) == [3, 8, 1, 4, 5, 77], "Целые числа"
    assert unique_func2([1, 3, 's'], 'd', 6, 5, 7, 's', seen =[3, 8]) == [3, 8, 1, 's', 'd', 6, 5, 7], "Список и произвольные аргументы"
    assert unique_func2([1, 3, 's'], 'd', 6, 5, 7, 's') == [1, 3, 's', 'd', 6, 5, 7], "Список и произвольные аргументы, без seen"
    assert unique_func2([1, 4.5, 5, 5, 5, 3, 77, 4], seen =[3, 'g', 8]) == [3, 'g', 8, 1, 4.5, 5, 77, 4], "Два списка"
    assert unique_func2('f', [1, 4, 5, 5, 5, 3, 4], seen=[3, 8]) == [3, 8, 'f', 1, 4, 5], "Произвольный элемент и список"
    assert unique_func2('f', seen=[3, 8]) == [3, 8, 'f'], "Произвольный элемент и список"
