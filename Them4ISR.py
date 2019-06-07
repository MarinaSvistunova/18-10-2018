# метод вставки
def insertionSort(mas = []):
    n = len(mas)
    for i in range(1, n):
        elChange = mas[i]
        k = i - 1
        while ((k >= 0)&(mas[k] > elChange)):
            mas[k + 1] = mas[k]
            k -= 1
        mas[k + 1] = elChange
    return mas

# a = [3, 7, 4, 9, 5, 2, 6, 1, -1, -8, 34, -35, 3425345, -345435243]
# print(insertionSort(a))

# разделение списка на два списка по признаку
def separateList(mas = []):
    mas1 = []
    mas2 = []
    for i in mas:
        if (i >= 0):
            mas1 += [i]
        else:
            mas2 += [i]
    return mas, mas1, mas2

# print(separateList(a))

class Arrays:

    def __init__(self, i = 0):
        d = int(input('Введите количество множеств: '))
        f = [[] for i in range(d)]
        print('Введите элементы множеств без запятых через пробел, каждое множество записывается с новой строки')
        for i in range(d):
            k = input().split(' ')
            f[i] += k
        # print(f)
        operation = input('Введите одну из операций: объединение, пересечение или вычитание ')
        if operation == 'объединение':
            print(self.grouping(*f))
        if operation == 'пересечение':
            print(self.crossing(*f))
        if operation == 'вычитание':
            print(self.substraction(*f))

    def grouping(self, *iterable, seen=[]):
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

    def crossing(self, *iterable, seen=[]):
        if len(seen) == 0:
            seen = list()
        k = 0
        for item in iterable[0]:
            for i in range(1, len(iterable)):
                if item not in iterable[i]:
                    k = 1
            if k == 0:
                seen.append(item)
            else:
                k = 0
        return list(seen)

    def substraction(self, *iterable, seen=[]):
        if len(seen) == 0:
            seen = iterable[-1]
        seen3 = list()
        for i in range(len(iterable) - 2, -1, -1):
            seen2 = iterable[i]
            for item in seen2:
                if item not in seen:
                    seen3.append(item)
            seen = seen3
            seen3 = list()
        return list(seen)

Arrays()




#
# def separateDict(d = {}):
#     '''+
#     деление массива по четности значений
#     '''
#     list = d.items()
#
#
# # плавная сортировка
# # def sortNumLeonardo(a, b):
# #     check = {1: 1, 2: 3, 3: 5, 4: 9, 5: 15}
# #     if (b == check.get(a - 1) or b == check.get(a + 1)):
# #         return 1
# #     else:
# #         return -1
# #
# # def smoothSort(mas = []):
# #     n = len(mas)
# #     firstMas = [mas[0]]
# #     secondMas = []
# #     for i in range(1, n):
# #         if sortNumLeonardo(len(firstMas), len(secondMas)) == 1:
# #             firstMas += [secondMas]
# #             firstMas += mas[i]
# #             secondMas = []
# #             maxEl
# #     pass