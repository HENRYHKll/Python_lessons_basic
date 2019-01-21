# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_list = [1, 1]
    for i in range(2, m):
        f_n = fib_list[i-1] + fib_list[i-2]
        fib_list.append(f_n)
    return fib_list[n:m]

print(fibonacci(0, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    inter_list = list(origin_list)
    sorted_list = []
    for i in origin_list:
        a = min(inter_list)
        sorted_list.append(a)
        inter_list.remove(a)
    return sorted_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def fil(fun, seq):                              
    new_seq = []
    x = 0
    for x in seq:
        if fun(x) is True:
            new_seq.append(x)
    return new_seq


print(fil((lambda x: x%2 == 0), [1, 3, 6, 89, 23, 44]))  

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
x1 = int(input("Введите x1= "))
y1 = int(input("Введите y1= "))
x2 = int(input("Введите x2= "))
y2 = int(input("Введите y2= "))
x3 = int(input("Введите x3= "))
y3 = int(input("Введите y3= "))
x4 = int(input("Введите x4= "))
y4 = int(input("Введите y4= "))


if((x1 - x2 == x3 - x4) and (y1 - y2 == y3 - y4)) or ((x2 - x3 == x4 - x1) and (y2 - y3 == y4 - y1)):
    print('Параллелограмм')
else:
    print("Не Параллелограмм")

