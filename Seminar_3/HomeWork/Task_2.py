# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample      

def get_list (amount):
    new_list = sample(range(1,amount+1), k=amount)  # создание произвольного списка с произвольными значениями
    return new_list

def product_pair (some_list):
    list_len = len(some_list)
    length = 0
    if list_len % 2 == 0:
        length = list_len/ 2
    else:
        length = list_len / 2 + 1

    for i in length:
        list_2 = some_list[i] * some_list[list_len - 1 - i]
        print(list_2)

list_1 = get_list(int(input("Введите число: ")))
print(list_1)
product_pair(list_1)