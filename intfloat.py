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


num = int(input())

a = num // 100 # Первая цифра числа
b = (num % 100) // 10 # Средняя цифра числа
c = num % 10 # Последня цифра числа 

more = (max(a, b, c,))
less = (min(a, b, c))
mid = ( a + b + c) - more - less
if more - less == mid or more + less == mid:
    print("Число интересное")
else:
    print("Число неинтересное")


# print(more, less)
# mid = num - more - less

# if mid == more + less or more - less:
#     print("Число интересное")
# else:
#     print("Число неинтересное")