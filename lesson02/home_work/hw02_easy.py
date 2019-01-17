__author__ =  'Генрих'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruids_list = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Дыня']
n = [1, 2, 3, 4, 5] 
for i in n:
    print('{1}. {0:>8}' .format(fruids_list[i - 1], n[i - 1]))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random
lists_1 = [random.randint(1, 10) for _ in range(6)]
print('Cписок 1', lists_1)
lists_2 = [random.randint(5, 15) for _ in range(6)]
print('Cписок 2', lists_2)
for i in lists_2:
	if i in lists_1:
		lists_1.remove(i)
print('Изменненый первый список:', lists_1)
#Тут стоит сказать иногда он и ничего не изменяет, о великий рандом( но мы же знаем что это наигроныая случайность ;) ) 


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

from random import sample
list = sample(range(-100, 100), 20)
print("Список случайных числе:",list)
new_lists = []
for i in list:
    if i % 2 == 0:
        new_lists.append(i / 4)
    else:
        new_lists.append(2 * i)
print("Готовый список:", new_lists) 
#эту задачу можно элегатнее решить веремени нет( 
