# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)

# print('Цикл завершен')

# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBBB")
# print("E")
# for i in range(9):
#     print("TTTTT")
# print("G")
# word = input()
# q = int(input())
# for i in range(q):
#     print(word)

# total = 0
# for i in range(3):
#     total = total - i
#     print(total)



# x = input()  # ПОВТОРЯЙ ЗА МНОЙ
# for i in range(10):
#     print(i, x)



# from math import pow 
# x = int(input())
# for i in range(x + 1):
#     x2 = pow(i, 2)
#     print(f"Квадрат числа {i} равен {x2}")


# n = int(input())
# for i in range(n):
#     print('*' * (n - i))

# m = float(input())
# p = int(input())
# n = int(input())
# p /= 100
# for i in range(n):
#     print(i + 1, m)
#     m += m * p

# m = int(input()) # включил в список последнее заданое число
# n = int(input())
# for i in range(m, n + 1):
#     print(i)

# n = int(input())  ТАБЛИЦА УМНОЖЕНИЯ
# for i in range(1, 11):
#     x = n * i 
#     print(f"{n} x {i} = {x}")


# m = int(input())
# n = int(input())

# if m or n % 17:

# m, n = int(input()), int(input())

# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 3 and 5 == 0:
#         print(i)

# m, n = int(input()), int(input())
# if m % 2 == 0 and n % 2 == 0:
#     for i in range(m - 1, n - 1, -2):
#         print(i)
# else:
#     for i in range(m, n, -2):
#         print(i)

# m, n = int(input()), int(input())
# for i in range(m - 1 + m % 2, n - 1, -2):
#     print(i)

# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# elif m > n:
#     for i in range(m, n - 1, -1):
#         print(i)
# elif m == n:
#     print(m)

# counter0 = 0    # ПОДСЧЕТ КОЛ-ВА РАЗ
# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#     if num == 0:
#         counter0 = counter0 + 1
# print(f"Кол-во чисел больше 10, вводилось {counter} раз ")
# print(f"Было введено кол-во нулей {counter0} раз")

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(f"Кол-во числе {counter} которым квадрат равно 4")


# total = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
# print(f"Сумма чисел больше 10 является {total}")

# total = 0
# for i in range(1, 101):
#     total = i + total
# print(f' Сумма равна ')

# total = 0 
# for i in range(10):
#     num = int(input())
#     total = total + num
# average = total / 10
# print(f'Среднее значение total = {average}')

# largest = 0
# for _ in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print(f"Наибольшее число = {largest}")

# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num

# print('Наибольшее число равно', largest) 

# smalest = int(input())
# for i in range(5):
#     num = int(input())
#     if num < smalest:
#         smalest = num
# print('Наименьшее число равно', smalest) 

# largest = int(input())
# smalest = largest
# for i in range(4):
#     num = int(input())
#     if num > largest:
#          largest = num
#     if num < smalest:
#          smalest = num
# print(smalest, largest)

# largest = None
# smallest = None

# for i in range(5):
#   num = int(input())
#   if largest is None or num > largest:
#     largest = num
#   if smallest is None or num < smallest:
#     smallest = num
# print(smallest, largest)




# prod = 1
# for i in range(-7, -3, 1):
#     if i < -5:
#         prod = prod * i
# print(prod)





# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
# if num == 1:
#     print('Это единица, она не простая и не составная') 
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')




# a = int(input())
# b = int(input())
# counter = 0
# for i in range(a, b + 1):
#     if i % 10 == 4 or i % 10 == 9:
#         counter += 1
# print(counter)



# n = int(input()) # переменная n
# total = 0 # счетчик с изначальным значением 0
# for _ in range(n):
#     num = int(input())
#     total += num
# print(total)



# from math import log                  ТУТ ПРАВИЛЬНО
# total = 0  
# n = int(input())
# for i in range(1, n + 1):
#     total += 1 / i
# print(total - log(n))
#     # total +=num




# n = int(input())                          СУММА ЧИСЕЛ 2
# total = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         total = total + i
# print(total)
                                    # ОПТИМИЗИРОВАННЫЙ КОД НИЖЕ

# n = int(input())
# sm = 0
# for i in range(5, n + 1, 10):
#     sm += i
# print(sm)


# for i in range(1, 6 + 1):
#     print("*" * i)

# n = int(input())
# for i in range(n):
#     print('*' * (n - i))


# from math import factorial             ФАКТОРИАЛ ЧИСЕЛ
# total = 1
# n = int(input())
# for i in range(1, n + 1):
#     total = i * total
# print(total)

# from math import factorial
# n = int(input())
# print(factorial(n))


# total = 1                             ИЗБЕГАТЬ ЧИСЛО 0
# for i in range(1, 10 + 1):
#     num = int(input())
#     if num != 0:
#         total = total * num
# print(total)


# n = int(input())                      #Сумма делителей

# total = 0 
# for i in range(1, n + 1):
#     if n % i == 0:
#         total = total + i
# print(total)




# total = 0                              # ТОЛЬКО ЧЕТНЫЕ ЧИСЛА ДВА РЕШЕНИЯЯ 
# for i in range(10):
#     a = int(input())
#     if a % 2 == 0:
#         total = total + 1
# if total == 10:
#     print("YES")
# else:
#     print("NO")

# flag = 'YES'
# for _ in range(10):
#     n = int(input())
    
#     if n % 2 == 1:
#         flag = 'NO'

# print(flag)


#                     #   ЗНАКОЧЕРЕДУЮЩАЯ СУММА
# total = 0
# n = int(input())
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total -= i
#     elif i % 2 == 1:
#         total += i
# print(total)




#  largest = 0
# for _ in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print(f"Наибольшее число = {largest}")

# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num

# print('Наибольшее число равно', largest) 

# smalest = int(input())
# for i in range(5):
#     num = int(input())
#     if num < smalest:
#         smalest = num
# print('Наименьшее число равно', smalest) 

# largest = int(input())
# smalest = largest
# for i in range(4):
#     num = int(input())
#     if num > largest:
#          largest = num
#     if num < smalest:
#          smalest = num
# print(smalest, largest)

# largest = None
# smallest = None

# for i in range(5):
#   num = int(input())
#   if largest is None or num > largest:
#     largest = num
#   if smallest is None or num < smallest:
#     smallest = num
# print(smallest, largest)

# largest = None
# largest2 = None
# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if largest is None or num > largest:
#         largest2 = largest
#         largest = num
#     elif largest2 is None or num > largest2:
#         largest2 = num  
# print(largest)
# print(largest2)

f1 = 0
f2 = 1

n = int(input())
for i in range(n):
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")
    