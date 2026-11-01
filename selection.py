# ИЗУЧЕНИЕ IF ELSE

# answer = input("Какой язык программированния мы изучаем?")

# if answer == 'Python':
#     print("Все верно! Мы изучаем Пайтон")
# else:
#     print('Не совсем правильный ответ') # в случае если ответ не "Пайтон"

# num1 = int(input("Введите число 1: "))
# num2 = int(input('Введите число 2: '))

# if num1 < num2:
#     print(num1, "меньше чем:", num2)
# if num1 > num2:
#     print(num1, 'больше чем', num2)

# if num1 == num2:
#     print(num1, 'равно', num2)
# if num1 != num2:
#     print(num1, 'неравны', num2)


# age = int(input())
# if 3 <= age <= 6:
#     print('Вы ребёнок')


# num = int(input())

# last_digit = num % 10
# first_digit = num // 10

# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')


# num1, num2 = int(input()), int(input())

# counter = 0
# if num1 % 2 == 0:
#     counter = counter + 1
# if num2 % 2 == 0:
#     counter = counter + 1

# print(counter)


# password = input()
# print("Введите пароль еще раз для проверки")
# password1 = input()

# if password == password1:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')



# num1 = int(input())

# if num1 % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# age = int(input())

# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# a = int(input())
# b = int(input())

# if a <= b:
#     print(a)
# else:
#     print(b)


# a = int(input())
# b = int(input())
# c = int(input())

# if a - b == b - c:
#     print('YES')
# else:
#     print('NO')



# num = int(input())   РАВНОСТЬ 1614

# a = num // 1000
# b = (num % 1000) // 100
# c = (num % 100) // 10
# d = num % 10

# if a + d == b - c:
#     print('ДА')
# else:
#     print("НЕТ")


# a = int(input())
# b = int(input())
# c = int(input())

# counter = 0
# if a % 2 == 0:
#     counter = counter + 1
# if b % 2 == 0:
#     counter = counter + 1
# if c % 2 == 0:
#     counter = counter + 1
#     print(counter)
# if a < 0 and b < 0 and c < 0:
#     print(0)



# a = int(input())
# b = int(input())
# c = int(input())

# if a > 0:
#     a = a
# else:
#     a = 0
# if b > 0:
#     b = b
# else:
#     b = 0
# if c > 0:
#     c = c
# else:
#     c = 0
# print(a + b + c)


# a, b, c = int(input()), int(input()), int(input())  #ВЫЧИСЛЕНИЕ СУММЫ ПОЛОЖИТЕЛЬНЫХ ЧИСЕЛ
# total = 0 
# if a > 0:
#     total = total + a
# if b > 0:
#     total = total + b
# if c > 0:
#     total = total + c
# print(total)


# 

# age = int(input())

# if age <= 13:
#     print('детство')
# if age >= 14 and age <=24:
#     print('молодость')
# if age >= 25 and age <=59:
#     print('зрелость')
# if age >= 60:
#     print('старость')



# a = int(input()) # ПОИСК МИНИМАЛЬНОГО ЧИСЛА ИЗ 4-ЕХ
# b = int(input())
# c = int(input())
# d = int(input())

# if a < b:
#     min_ab = a
# else:
#     min_ab = b

# if c < d:
#     min_cd = c
# else:
#     min_cd = d
# if min_ab < min_cd:
#     print(min_ab)
# else:
#     print(min_cd)


# print(min(int(input()), int(input()), int(input()), int(input())))

# print("*"*17)
# print("*", "*", sep="               ")
# print("*", "*", sep="               ")
# print("*"*17)



# a = int(input()) 
# b = int(input())
# num = (a + b)**2
# num1 = a**2 + b**2
# print("Квадрат суммы", a, "и", b, "равен", num)
# print("Сумма квадратов", a, "и", b, "равна", num1)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# num = a**b + c**d
# print(num)

a = int(input())
print(a + (a * 11) + (a * 111))