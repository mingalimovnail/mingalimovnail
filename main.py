#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input("Привет, Введи значение a \n"))
b = int(input("Привет, Введи значение b \n"))
c = int(input("Привет, Введи значение c \n"))
print(' {}x^2 + {}x + {} = 0'.format(a, b, c))
D = b * b - 4 * a * c

if D < 0:
    print( "Нет действительных корней")
elif D == 0:
    x = -b / (2 * a)
    print(f"Уравнение имеет одно решение: \n {x}")
else:
    x1 = (-b + D) / 2 * a
    x2 = (-b - D) / 2 * a
    print(f"Уравнение имеет два решения: \n {x1} \n {x2} ")

