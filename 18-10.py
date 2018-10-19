def main(*lst):
    '''Функция для сортировки списка
        Переданное в функцию значение проверяется на соответствие одному из типов,
        в зависимости от результатов проверки список преобразовывается
        Значения вводятся с клавиатуры, поэтому изначально имеют тип str
        '''
    lst2 = [0] * len(lst)
    for k in range(len(lst)):
        if lst[k].isdigit():
            lst2[k] = int(lst[k])
        elif lst[k] == 'True' or lst[k] == 'False':
            if lst[k] == 'True':
                lst2[k] = True;
            elif lst[k] == 'False':
                lst2[k] = False;
            lst2[k] = lst2[k]
        else:
            try:
                float(lst[k])
                lst2[k] = float(lst[k])
            except ValueError:
                lst2[k] = lst[k]
    return sorted(lst2)

a = [i for i in input().split(' ')]
print(main(*a))

if __name__ == '__main__':
    assert main('1', '8', '2', '99', '5') == [1, 2, 5, 8, 99],\
          "Сортировка по возрастанию целых чисел"
    assert type(main('1', '8', '2', '99', '5')) == list,\
          "Тип"
    assert main('1.3', '8.1', '2.1', '1.1', '99.3', '5.4') == [1.1, 1.3, 2.1, 5.4, 8.1, 99.3], \
        "Сортировка по возрастанию чисел с плавающей запятой"
    assert main('True', 'False', 'False', 'True') == [False, False, True, True], \
        "Сортировка по возрастанию значений логических типов"
    assert main('love', 'with my-myself', 'I am', 'in') == ['I am', 'in', 'love', 'with my-myself'], \
        "Сортировка по возрастанию строк"