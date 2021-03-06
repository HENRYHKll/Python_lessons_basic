# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random
import math

lists_1 = [random.randint(4, 25) for _ in range(5)]
print('Генерируем список', lists_1)

lists_new = []
for i in lists_1:
    if i > 0 and int(math.sqrt(i)) == math.sqrt(i): 
        lists_new.append(int((math.sqrt(i))))
print('Список корней если они существуют: ', lists_new)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input('Ввелите дату (ДД.ММ.ГГГГ): ')
date = date.split('.')

days = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое',
        'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадацать четвёртое',
        'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября',
          'октября', 'ноября', 'декабря']

day = days[int(date[0]) - 1]
month = months[int(date[1]) - 1]
year = date[2]

print(day, month, year, 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input('Какое количество элементов вы жилаете: '))
list_1 = [random.randint(-100, 100) for _ in range(n)]
print('Пожалуста:', list_1)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random
lists = [random.randint(1, 10) for _ in range(10)]
print('Список', lists)
list_new = set(lists)
print('Новый список', list_new)
#тут наверное я запутался
