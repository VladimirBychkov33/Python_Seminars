# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import sample      

def get_list (amount):
    new_list = sample(range(1,(amount+1)*3), k=amount)  # создание произвольного списка с неповторяющимися значениями
    return new_list
    

def sum_odd (some_list):
    result = 0
    for i in some_list[::2]:   # берём из списка только четные индексы
        result = result + i
    print(result)


list_1 = get_list(int(input("Введите число: ")))
print(list_1)
sum_odd(list_1)