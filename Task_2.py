# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# x1 = 5, x2 = 15
from random import randint
x1 = 5
x2 = 15
lst = []
lst = [randint(-10,20) for i in range(20)]
print(lst)

for i in range(len(lst)):
    if x1 <= lst[i] <= x2:
        print(i, end = ' ')

