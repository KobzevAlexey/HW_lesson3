# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input('Введите число: '))

fib_pos = []
fib_otr = []
a, b = 0, 1
c, d = 0, 1
for i in range(num):
    a, b = b, a + b
    fib_pos.append(a)
    c, d = d, c - d
    fib_otr.append(c)

fib_otr.reverse()
print(f'{*fib_otr, 0, *fib_pos}')
