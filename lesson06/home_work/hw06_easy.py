# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        # длина стороны
        def side(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        self.AB = side(A, B)
        self.BC = side(B, C)
        self.CA = side(C, A)
    # метод для площади
    def S(self):
        #полупериметр
        hp = self.P() / 2
        # площадь
        return math.sqrt(hp * (hp - self.AB) * (hp - self.BC) * (hp - self.CA))
    # метод периметра
    def P(self):
        return self.AB + self.BC + self.CA
    # метод высоты
    def H(self):
        return self.S() / (self.AB / 2)
t_1 = Triangle((0, 0), (0, 4), (4, 0))
print('Сторона А: ', t_1.AB)
print('Сторона B: ', t_1.BC)
print('Сторона C: ', t_1.CA)
print('Площадь: ', t_1.S())
print('Высота: ', t_1.H())
print('Периметр: ', t_1.P())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapeze:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # длина стороны
        def side(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        self.AB = side(A, B)
        self.BC = side(B, C)
        self.CD = side(C, D)
        self.DA = side(D, A)
        # вариант площади через площадь двух составляющих ее треугольников
        def S(a, b, c):
            hp = (a + b + c) / 2
            return math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
        self.D_AC = side(self.C, self.A)
        self.D_BD = side(self.B, self.D)
        self.P = self.AB + self.BC + self.CD + self.DA
        self.S = S(self.AB, self.D_BD, self.DA) + S(self.D_BD, self.BC, self.CD)
        # вариант площади по четырем сторонам
        def S1(a, b, c, d):
            return (a + b) / 2 * math.sqrt(c**2 - (((a - b)**2 + c**2 - d**2) / 2 * (a - b))**2)
        # для равнобедренной можно еще через высоту, тут не привожу, времнеи не хватит
        self.S1 = S1
Trapeze_1 = Trapeze((0, 0), (10, 0), (8, 4), (2, 4))
if Trapeze_1.D_AC == Trapeze_1.D_BD and Trapeze_1.BC == Trapeze_1.DA:
    print("Трапеция равнобедренная")
else:
    print("Трапеция НЕ равнобедренная")
print('Сторона A: ', Trapeze_1.AB)
print('Сторона B: ', Trapeze_1.BC)
print('Сторона C: ', Trapeze_1.CD)
print('Сторона D: ', Trapeze_1.DA)
print('Периметр: ', Trapeze_1.P)
print('Площадь: ', Trapeze_1.S)
print('Площадь1: ', Trapeze_1.S1)

