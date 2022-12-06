# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [2, 3, 7, 3, 8, 5, 6]
if len(lst) % 2 == 0:
    for i in range(len(lst) // 2):
        print(lst[i] * lst[len(lst) - 1 - i])
if len(lst) % 2 != 0:
    for i in range(len(lst)):
        print(lst[i] * lst[len(lst) - 1 - i])
        if i == len(lst) // 2:
            break
