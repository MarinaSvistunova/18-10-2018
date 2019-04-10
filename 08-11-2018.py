# Свистунова Марина, 2ИВТ
# 08.11.2018, Лабораторная работа

import math
z = list(map(lambda *x: tuple([i for i in x]), range(1,6), range(5,12), range(11,18), range(1,6)))
print(z)
p = [x**2 for x in [1,3,4,15]]
print(p)
pt = [1, 4, 5, -6]
k = [int(math.sqrt(x*x)) for x in pt]
print(k)
k2 = [abs(x) for x in pt]
print(k2)

mass