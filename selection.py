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


a = int(input())
b = int(input())
c = int(input())

if a - b == b - c:
    print('YES')
else:
    print('NO')