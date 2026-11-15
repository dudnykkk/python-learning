# a = 13
# b = 7

# total = a + b
# diff = a - b
# prod = a * b
# div1 = a / b
# div2 = a // b
# mod = a % b
# exp = a ** b

# print(a, '+', b, '=', total)
# print(a, '-', b, '=', diff)
# print(a, '*', b, '=', prod)
# print(a, '/', b, '=', div1)
# print(a, '//', b, '=', div2)
# print(a, '%', b, '=', mod)
# print(a, '**', b, '=', exp)


# print(25_000)
# print(25_000 == 25000)


# s = float(input()) # ДВЕ СТАРУШКИ РАСЧЕТ СКОРОСТИ 
# v1 = float(input())
# v2 = float(input())
# print(s / (v1 + v2))

# s = float(input())    # ОБРАТНОЕ ЧИСЛО 
# if s == 0: 
#     print("Обратного числа не существует")
# else:
#     print(s ** -1 and 1 / s)


# num = float(input())

# t = 5 / 9 * (num - 32)
# print(t)

# num = float(input())
# age = 10.5
# if num <= 2:
#     print(age * num)
# else:
#     print(21 + (num - 2) * 4)

# num = float(input())   # ПОИСК ДРОБНОГО ЧИСЛА (ОСТАТКА)

# a = int(num)
# b = num - a
# print(b)

# num = float(input())

# a = num - int(num)
# b = int(a * 10)
# print(b)



# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

# print("Наименьшее число =", min(a, b, c, d, e))
# print("Наибольшее число =", max(a, b, c, d, e))


# a1 = float(input())
# a2 = float(input())
# a3 = float(input())
# a4 = float(input())
# a5 = float(input())

# print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))


# num = int(input())

# a = num // 100 # Первая цифра числа
# b = (num % 100) // 10 # Средняя цифра числа
# c = num % 10 # Последня цифра числа 

# more = (max(a, b, c,))
# less = (min(a, b, c))
# mid = ( a + b + c) - more - less
# if more - less == mid or more + less == mid:
#     print("Число интересное")
# else:
#     print("Число неинтересное")


# print(more, less)
# mid = num - more - less

# if mid == more + less or more - less:
#     print("Число интересное")
# else:
#     print("Число неинтересное")


# a = int(input())
# b = int(input())
# c = int(input())

# more = max(a, b, c)
# less = min(a, b, c)
# mid = (a + b + c) - less - more
# print(more, mid, less, sep="\n" )

# p1 = int(input()) Манхэттенское расстояние ПО МОДУЛЮ ABS
# p2 = int(input()) 
# q1 = int(input())
# q2 = int(input())

# print( abs(p1 - q1) + abs(p2 - q2))

# print('I love C++' * 0 == '') # ВЫВОДИТ TRUE

# # ЕСЛИ НАМ НУЖНО ВЫВЕСТИ "-" в большо кол-ве можно СТРОКУ УМНОЖИТЬ НА ЧИСЛО
# print('-' * 100)

# print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

# # Hello <введённое имя> <введённая фамилия>! You have just delved into Python

# name = input()
# sname = input()

# print(f"Hello {name} {sname}! You have just delved into Python" )

# a = input()   #КОЛ-ВО БУКВ В СЛОВЕ
# b = len(a)

# print(f"Футбольная команда {a} имеет длину {b} символов")

# a, b, c = input(), input(), input()

# a1 = len(a)
# b1 = len(b)
# c1 = len(c)

# more = max(a1, b1, c1)
# less = min(a1, b1, c1)

# if less == a1:
#     print(a)
# elif less == b1:
#     print(b)
# elif less == c1:
#     print(c)
# if more == a1:
#     print(a) 
# elif more == b1:
#         print(b)
# elif more == c1:
#     print(c)

# a, b, c = len(input()), len(input()), len(input())
# if (2 * b - c - a) * (2 * c - b - a) * (2* a - b - c) == 0:
#     print("YES")
# else:
#     print("NO")

# s = input()
# if len(s) == 1 and s in 'aeiou':
#     print('YES')

# s = input()
# if "синий" in s:
#     print("YES")
# else:
#     print('NO')


# day = input()  #

# if "суббота" in day or "воскресенье" in day:
#     print("YES")
# else:
#     print('NO')

# #ПРАВИЛЬНЫЙ ЭМЭИЛ

# post = input()
# if '@' in post and '.' in post:
#     print('YES')
# else:
#     print('NO')




# *************************** MATH ****************************

# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз

# from math import *

# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз

# print(num1)
# print(num2)
# print(num3) # ДЛЯ УДОБСТВА ЧТОБЫ НЕ ПРОПИСЫВАТЬ import math можно from import math *


# ПЛОЩАДЬ И ДЛИНА КРУГА

# R = float(input())
# s = 3.141592653589793 * pow(R, 2)
# c = 2 * 3.141592653589793 * R
# print(s, c, sep="\n")

# from math import pi, pow

# R = float(input())
# print(pi * pow(R,2))
# print(2 * pi * R)

# from math import *
# # x = float(input())
# print( floor(x) + ceil(x))

# 2.0
# 2.5
# 44.155
# 100.50



# from math import *  # ЕВКЛИДОВО РАССТОНИЕ
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())

# p = sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print(p)


# from math import * # ТРИГОНОМЕТРИЧЕСКОЕ ВЫРАЖЕНИЕ
# x = float(input())
# r = radians(x) #(x * pi / 180)
# x1 = sin(r) + cos(r) + tan(r) ** 2
# print(x1)


 
# from math import *   # Правильный многоугольник
# n = float(input())
# a = float(input())
# s = (n * pow(a,2)) / (4 * tan(pi / n))
# print(s)


            # СРЕДНИЕ ЗНАЧЕНИЯ
# from math import sqrt, pow

# a, b = float(input()), float(input())

# mid_ab = (a + b) / 2
# mid_geo = sqrt(a * b)
# mid_gar = (2 * a * b) / (a + b)
# mid2ab = sqrt((a**2 + b**2) / 2)

# print(mid_ab, mid_geo, mid_gar, mid2ab, sep="\n")


# Квадратное уравнение 
from math import sqrt, pow
a, b, c = float(input()), float(input()), float(input())

# n = a * pow(x, 2) + b * x + c = 0

d = pow(b, 2) - 4 * a * c
if d < 0:
    print("Нет корней")
elif d == 0: # имеет корень
    x = -b / (2 * a)
    print(x)
elif d > 0: # имеет два действительных корня
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))