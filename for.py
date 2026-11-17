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

m = float(input())
p = int(input())
n = int(input())
p /= 100
for i in range(n):
    print(i + 1, m)
    m += m * p
