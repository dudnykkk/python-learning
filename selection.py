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

# a = int(input())
# print(a + (a * 11) + (a * 111))


# x = int(input())
# y = int(input())

# if x > 2 or y >= 10:
#     print("Правда")
# else:
#     print("ноу")
                  

# river1 = 'Хуанхэ'
# river2 = 'Темза'

# if (river1 == 'Хуанхэ' or river1 == 'Дунай') and river2 == 'Тигр':
#     print("ПАРАДА")
# else:
#     print("NO")


# a = int(input())

# if a > -1 and a < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# a = int(input())
# if a <= -3 or a >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# a = int(input())
# if (-30 < a <= -2) or (7 < a <= 25):
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# num = int(input())  
# if (1000 <= num <=9999) and (num % 7 == 0 or num % 17 == 0):
#     print("YES")
# else:
#     print("NO")


# a+b>c НЕРАВНОРОЖДЕННЫЙ ТРЕУГОЛЬНИК
# a+c>b
# b+c>a

# a = int(input())
# b = int(input())
# c = int(input())

# if (a + b > c) and (a + c > b) and b + c > a:
#     print("YES")
# else:
#     print("NO")


# print("Повтор")

# year = int(input())

# if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
#     print("YES")
# else:
#     print("NO")
# узнать какой год високосный
# year = int(input())  # водим какой год хотим узнать високостный или нет
  # год високостный это год который делится на 4 но не делится на сто и делится на 400.
  # решение через метод if else



# x1 = int(input())    # ХОД КОРОЛЯ
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if (x1 >= x2 -1 and x1 <= x2 +1) and (y1 >= y2 -1 and y1 <= y2 +1):
#     print("YES")
# else:
#     print("NO")


#     # put your python code here
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print("YES" if (a-1==c or a+1==c or a==c) and (b-1==d or b+1==d or b==d) else "NO")




# print("повтор")
    
    
    # (1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <=8)


# angle = 720

# if angle % 90 == 0:
#     if angle == 0:
#         print('Нулевой')
#     elif angle == 90:
#         print('Прямой')
#     elif angle == 180:
#         print('Развёрнутый')
# else:
#     if 0 < angle < 90:
#         print('Острый')
#     elif 90 < angle < 180:
#         print('Тупой')
#     elif 180 < angle < 270:
#         print('Выпуклый')
#     else:
#         print('Ни острый, ни тупой, ни выпуклый')


# n = int(input())    # СКОРОСТЬ ФЛЕША И ЗУМА
# k = int(input())

# if n > k:
#     print("NO")
# elif n < k:
#     print("YES")
# else:
#     print("Don't know")

# a = int(input())   # ПРОВЕРКА КАКОЙ ВИД ТРЕУГОЛЬНИКА
# b = int(input())
# c = int(input())

# if a == b == c:
#     print("Равносторонний")

# elif a == b or b == c or a == c:
#     print("Равнобедренный")

# elif a != b and b != c and c != a:
#     print("Разносторонний")
# else:
#     print("Возможно ты ввел текст")


# a = int(input())    #  ПОИСК СРЕДНЕГО ЧИСЛА ИЗ 3 ЗАДАННЫХ
# b = int(input())
# c = int(input())

# if a <= b <= c:
#     print (b)
# elif a <= c <= b:
#     print(c)
# elif b <= a <= c:
#     print(a)
# elif b <= c <= a:
#     print(c)
# elif c <= b <= a:
#     print(b)
# elif c <= a <= b:
#     print(a)


# ВЫЧЕСЛЕНИЕ КОЛ-ВА ДНЕЙ В МЕСЯЦЕ

# a = int(input())

# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print("31")
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print("30")
# else:
#     print("28")


# month = int(input())
# if month == 2:
#     print('28')
# else:
#     print(30 + (month + month // 8) % 2)

#ПРОВЕРКА ВЕСОВОЙ КАТЕГОРИИ БОКСЕРА

# a = int(input())

# if a < 60:
#     print("Легкий вес")
# elif a >= 60 and a < 64:
#     print("Первый полусредний вес")
# elif a >= 64 and a < 69:
#     print("Полусредний вес") 

a = int(input())
b = int(input())
c = input()

if c == "+":
    print(a + b)
elif c == "*":
    print(a * b)
elif c == "-":
    print(a - b)
elif c == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
else:
    print("Неверная операция")