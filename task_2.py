# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5.1, 10.01]
for i in range(len(lst)):
    lst[i] = lst[i] % 1
diff = max(lst) - min(lst)
print('%.2f' % diff)
